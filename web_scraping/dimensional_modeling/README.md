### Descripción de la Carpeta `data_normalization`

En esta carpeta, se documenta el proceso de normalización y modelado dimensional de la tabla principal `properties`. Inicialmente, tenemos una tabla general llamada `properties` que contiene todos los datos de las propiedades en alquiler. Para mejorar la estructura y eficiencia de los datos, llevamos a cabo los siguientes pasos:

1. **Normalización de la Tabla `properties`**:
   - La tabla `properties` se normaliza hasta la tercera forma normal (3NF) para eliminar redundancias y dependencias transitivas. Esto asegura que cada atributo no clave dependa únicamente de la clave primaria y no de otros atributos no clave.

2. **Modelado Dimensional**:
   - Utilizamos el modelado dimensional para organizar los datos en tablas más pequeñas y especializadas. Este enfoque facilita el análisis y la consulta de datos.
   - Se crean tres tablas dimensionadas:
     
     - `prop_facts`: Contiene los hechos principales de las propiedades, como el tamaño en metros cuadrados, el número de baños, habitaciones y el precio.
       https://github.com/elena210910/Web-scraping-PostgreSQL/blob/main/web_scraping/dimensional_modeling/SQL_prop_fact
       
     - `agenc_dim`: Contiene información sobre las agencias inmobiliarias, incluyendo el nombre de la agencia y el enlace a su sitio web.
       https://github.com/elena210910/Web-scraping-PostgreSQL/blob/main/web_scraping/dimensional_modeling/SQL_agenc_dim
       
     - `descrip_dim`: Contiene descripciones detalladas de las propiedades.
       https://github.com/elena210910/Web-scraping-PostgreSQL/blob/main/web_scraping/dimensional_modeling/SQL_descrip_dim

3. **Migración de Datos**:
   - Los datos de la tabla `properties` se migran a las nuevas tablas dimensionadas. Este proceso implica la transferencia de datos relevantes a cada una de las tablas especializadas.
   - La migración se realiza utilizando consultas SQL para asegurar que los datos se distribuyan correctamente y mantengan su integridad.
     https://github.com/elena210910/Web-scraping-PostgreSQL/blob/main/web_scraping/dimensional_modeling/SQL_Migracion_de_Datos

4. **Relaciones entre Tablas**:
   - Las tablas dimensionadas están relacionadas entre sí mediante claves foráneas. Por ejemplo, `prop_facts` actúa como la tabla central y tiene relaciones con `agenc_dim` y `descrip_dim` a través del atributo `id`.
   - Estas relaciones permiten realizar consultas complejas y obtener información detallada de manera eficiente.

Este proceso de normalización y modelado dimensional no solo mejora la estructura de los datos, sino que también optimiza el rendimiento de las consultas y facilita el mantenimiento de la base de datos. Aqui se puede observar el resultado final:  
https://github.com/elena210910/Web-scraping-PostgreSQL/blob/main/web_scraping/dimensional_modeling/rentalpropertiesdb%20-%20public%20-%20prop_facts.png

### NOTA
En este ejemplo, la tabla general `properties`  contiene solo 30 filas. Esto se ha hecho exclusivamente con fines demostrativos para mostrar el proceso de tratamiento de datos, su carga en PostgreSQL y la posterior normalización de las tablas. Este enfoque puede ser extremadamente útil y eficiente para manejar conjuntos de datos mucho más grandes.
