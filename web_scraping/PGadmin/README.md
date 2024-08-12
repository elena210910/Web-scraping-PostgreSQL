**Actualmente estamos en la segunda etapa,**
en la etapa de carga de datos tabulares en nuestra base de datos, 
donde podremos realizar diferentes operaciones analíticas utilizando el lenguaje de consultas SQL, 
lo cual es mucho más conveniente que realizar análisis en Excel, por ejemplo.

Así que… hemos hecho el parsing del sitio web y guardado los datos en formato xlsx (como mencioné, es mejor guardarlos en formato csv).
Si el archivo aún está guardado en formato Excel, conviértelo a csv como lo requiere PostgreSQL.


Ahora, según nuestra tabla obtenida del parsing, necesitamos crear una tabla en PostgreSQL, y esto es lo que obtenemos:


CREATE TABLE Properties (
    id SERIAL PRIMARY KEY,
    descripcion TEXT,
    precio VARCHAR(50),
    m2 INT,
    hab INT,
    banos FLOAT,
    agencia VARCHAR(255),
    enlace TEXT
);

Ten en cuenta que el precio, que es crucial para nuestros análisis,
debe guardarse con el tipo de datos VARCHAR, pero no te preocupes, lo cambiaremos más tarde. 
Así que hemos creado la tabla, ahora la tenemos en forma normal 1NF. 
El siguiente paso es cargar los datos de nuestra tabla en la tabla de PostgreSQL.

Ahora, carguemos los datos de nuestra tabla en la base de datos usando Python. 
Este código lo he guardado en la misma carpeta bajo el nombre CODE_PYTHON_SQL:   
https://github.com/elena210910/Web-scraping-PostgreSQL/blob/main/web_scraping/PGadmin/CODE_PYTHON_SQL

¡Y voilà! Nuestra tabla ahora está en PostgreSQL.!
https://github.com/elena210910/Web-scraping-PostgreSQL/commit/87e9f4b8e343e4e76585a2eb12a8be351d209e0e

Bueno, ahora pasemos al precio. Como mencioné anteriormente, actualmente está con el tipo de datos VARCHAR, y esto es lo que haremos:


