# Web-scraping-PostgreSQL
Web Scraping with Python and Adding to PostgreSQL

# Proyecto: Web Scraping de Sitio de Inmuebles y Carga de Datos en PostgreSQL

## Descripción del Proyecto

El objetivo de este proyecto es demostrar el proceso de web scraping de un sitio de inmuebles utilizando Python y la posterior carga de datos tabulares en PostgreSQL, asegurando que la tabla esté en la forma normal 1NF para facilitar el análisis.

## Descripción

En este proyecto, se realizó un web scraping de datos de alquiler de propiedades de uno de los sitios de inmuebles más populares en España. Para el ejemplo, se eligió una ciudad pequeña, donde hay alrededor de 30 apartamentos disponibles para alquiler. Sin embargo, es importante entender que en ciudades grandes como Madrid, hay más de 6000 propiedades en alquiler. En tales casos, es más conveniente analizar y estudiar los datos utilizando el lenguaje de consultas SQL.

## Principales Etapas del Proyecto

1. **Web Scraping**:
   - Uso de Python para extraer datos de alquiler de propiedades del sitio web seleccionado.
     https://github.com/elena210910/Web-scraping-PostgreSQL/tree/main/web_scraping
   
2. **Carga de Datos en PostgreSQL**:
   - Carga de los datos tabulares en la base de datos PostgreSQL en PGadmin , asegurando que la tabla esté en la forma normal 1NF.
     https://github.com/elena210910/Web-scraping-PostgreSQL/tree/main/web_scraping/PGadmin

3. **Modelado Dimensional y Normalización**:
   - Después de cargar los datos en la base de datos, se realizó la normalización de las tablas hasta la tercera forma normal (3NF) para mejorar la estructura y eficiencia de los datos.
   - Se crearon tablas dimensionadas (`descrip_dim`, `agenc_dim`, `prop_facts`) para organizar mejor los datos.
     https://github.com/elena210910/Web-scraping-PostgreSQL/tree/main/web_scraping/dimensional_modeling    

## Requisitos

- Python 3.x
- Librerías de Python: SELENIUM, Pandas.
- PostgreSQL (PGadmin, DBeaver)


