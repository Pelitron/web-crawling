import scrapy
from scrapy.crawler import CrawlerProcess

class WatchSpider(scrapy.Spider):
    name = 'watchspider'
    start_urls = ["https://www.creationwatches.com/products/seiko-75/"]
    custom_settings = {
        'FEED_FORMAT': 'json',
        'FEED_URI': 'watch_data.json'
    }

    def parse(self, response: scrapy.http.Response) -> dict:
        """
        Método de callback que se llama para manejar la respuesta
        descargada para la URL inicial.

        Args:
            response (scrapy.http.Response): La respuesta HTTP
                del servidor que contiene el contenido de la página.

        Yields:
            dict: Un diccionario que contiene la información extraída
                de cada reloj (imagen, nombre y precio).
        """
        
        def extract_image(result: scrapy.Selector) -> str:
            """Extrae la imagen del reloj.

            Args:
                result (scrapy.Selector): Bloque de producto.

            Returns:
                str: URL de la imagen del reloj (o None si no se encuentra).
            """
            return result.css("div.imgBox img::attr(src)").get()

        def extract_name(result: scrapy.Selector) -> str:
            """Extrae el nombre del reloj.

            Args:
                result (scrapy.Selector): Bloque de producto.

            Returns:
                str: Nombre del reloj (o None si no se encuentra).
            """
            return result.css("a.pro_titel::text").get()

        def extract_price(result: scrapy.Selector) -> str:
            """Extrae el precio del reloj.

            Args:
                result (scrapy.Selector): Bloque de producto.

            Returns:
                str: Precio del reloj (o None si no se encuentra).
            """
            return (result.css("div h3 del::text").get() or
                    result.css("div h3 span::text").get())

        def extract_item(result: scrapy.Selector) -> dict:
            """Extrae la información completa de un reloj.

            Args:
                result (scrapy.Selector): Bloque de producto.

            Returns:
                dict: Diccionario con 'image', 'name' y 'price'.
            """
            return {
                'image': extract_image(result),
                'name': extract_name(result),
                'price': extract_price(result)
            }

        items = map(extract_item, response.css("div.catalog_productBox"))
        yield from items

# Configuración y ejecución del crawler
process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
})

# Inicia el spider
process.crawl(WatchSpider)
process.start()
