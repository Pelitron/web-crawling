
#!pip install scrapy

import scrapy
from scrapy.crawler import CrawlerProcess

class WatchSpider(scrapy.Spider):
    """
    Spider de Scrapy para extraer información de relojes de la página web
    de Creation Watches.

    Attributes:
        name (str): Nombre del spider, utilizado para identificarlo.
        start_urls (list): Lista de URLs iniciales desde las que comenzará
            a extraer datos.
        custom_settings (dict): Configuraciones personalizadas para la
            salida de datos.
    """
    
    name = 'watchspider'
    start_urls = ["https://www.creationwatches.com/products/seiko-75/"]
    custom_settings = {
        'FEED_FORMAT': 'json',
        'FEED_URI': 'watch_data.json'
    }

    def parse(self, response):
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
        
        def extract_item(result):
            """
            Función interna para extraer datos de un producto.

            Args:
                result (scrapy.Selector): Un selector que representa
                    un bloque de producto.

            Returns:
                dict: Un diccionario con la imagen, nombre y precio
                    del reloj.
            """
            extract = {
                'image': result.css("div.imgBox img::attr(src)").get(),
                'name': result.css("a.pro_titel::text").get(),
                'price': (
                    result.css("div h3 del::text").get() or
                    result.css("div h3 span::text").get()
                )
            }
            return extract

        yield from map(extract_item, response.css("div.catalog_productBox"))

# Configuración y ejecución del crawler
process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
})

# Inicia el spider
process.crawl(WatchSpider)
process.start()
