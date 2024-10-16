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
        yield from (
            {
                'image': self.extract_image(result),
                'name': self.extract_name(result),
                'price': self.extract_price(result)
            }
            for result in response.css("div.catalog_productBox")
        )

    def extract_image(self, result: scrapy.Selector) -> str:
        """Extrae la imagen del reloj."""
        return result.css("div.imgBox img::attr(src)").get()

    def extract_name(self, result: scrapy.Selector) -> str:
        """Extrae el nombre del reloj."""
        return result.css("a.pro_titel::text").get()

    def extract_price(self, result: scrapy.Selector) -> str:
        """Extrae el precio del reloj."""
        return (result.css("div h3 del::text").get() or
                result.css("div h3 span::text").get())

# Configuración y ejecución del crawler
process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
})

# Inicia el spider
process.crawl(WatchSpider)
process.start()
