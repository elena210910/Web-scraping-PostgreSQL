**Web Scraping con Python** 

Esta carpeta contiene un ejemplo de un web scraper que recopila datos sobre alquileres de viviendas 
en la ciudad de Sabadell desde el sitio web HABITACLIA. 
HABITACLIA es uno de los principales sitios en el mercado inmobiliario en España. 
El scraper utiliza la biblioteca Selenium, que imita al máximo las acciones de un usuario real.

**Descripción**
[Codigo Python de web-scraper](https://github.com/elena210910/Web-scraping-PostgreSQL/blob/main/web_scraping/scraping_script.py)
El scraper recopila datos sobre alquileres de viviendas en la ciudad de Sabadell. 
(Se puede cambiar el enlace a cualquier otra ciudad, ya sea para ventas o alquileres). 
El sitio es dinámico y carga información a medida que se navega. Cuando todas las páginas han sido vistas y los datos recopilados en listas, 
el último paso es crear una tabla en Excel donde todo se organiza por descripción, m², baños, agencias u enlaces.

**Bibliotecas Utilizadas**

- **Selenium**: para la automatización del navegador e interacción con las páginas web.
- **Pandas**: para trabajar con datos y guardarlos en Excel.
- **Undetected Chromedriver**: para evitar la detección de la automatización del navegador.

**Enlace Excel para ver el resultado final** 
https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fraw.githubusercontent.com%2Felena210910%2FWeb-scraping-PostgreSQL%2Fmain%2Fweb_scraping%2Fhabitaclia.xlsx&wdOrigin=BROWSELINK

**Nota**
Es importante entender que este sitio es dinámico. A día de hoy, 7 de agosto de 2024, funciona correctamente, pero en una semana podría necesitar soporte técnico y algunos cambios. Por lo tanto, la necesidad de soporte técnico para estos scrapers web es un aspecto crucial. Para añadir la tabla a PostgreSQL mejor tener en formato csv, en ves de xlsx como la tengo yo en esta demostracion. 
