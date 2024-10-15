# web-crawling

# WatchSpider

WatchSpider es un spider de Scrapy diseñado para extraer información sobre relojes del sitio web Creation Watches. Este proyecto permite obtener datos como la imagen, el nombre y el precio de los productos de manera automatizada.

## Instalación

Asegúrate de tener Python y `pip` instalados en tu máquina. Luego, instala Scrapy ejecutando:

```bash
pip install scrapy
```

## Uso
Para ejecutar el spider, simplemente corre el siguiente comando en el terminal dentro del directorio del proyecto:

```bash

python -m scrapy runspider watch_spider.py
```

Esto iniciará el proceso de extracción y guardará los datos en un archivo llamado watch_data.json.

## Estructura del Proyecto
```bash

/watchspider
│
├── watch_spider.py  # Código fuente del spider
├── watch_data.json  # Archivo de salida con los datos extraídos
└── README.md        # Documentación del proyecto
```

## Detalles Técnicos

- Spider: WatchSpider
- Inicio de URL: https://www.creationwatches.com/products/seiko-75/
- Formato de Salida: JSON
- Datos Extraídos:
Imagen del reloj
Nombre del reloj
Precio del reloj

## Contribuciones

Si deseas contribuir a este proyecto, siéntete libre de abrir un "issue" o enviar un "pull request".

## Licencia

Este proyecto está bajo la Licencia GNU GENERAL PUBLIC LICENSE. Para más detalles, consulta el archivo LICENSE.

### Instrucciones para usar el README

1. Guarda este contenido en un archivo llamado `README.md` en el directorio raíz de tu proyecto.
2. Personaliza cualquier sección según sea necesario, como la información de licencia o detalles adicionales sobre la configuración.
