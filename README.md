# API Bike Santiago ( <img src="https://user-images.githubusercontent.com/66185308/219544687-7a92774b-c2bc-48cc-b9ff-efda4e7bf22a.png" width="80"> + <img src="https://user-images.githubusercontent.com/66185308/219544998-7c87fa3b-10e0-4ec1-bbf3-fdc52473a03d.png" width="80">  + <img src="https://user-images.githubusercontent.com/66185308/219545154-84a0c617-7ed1-4d7d-90fc-1ca6829732da.png" width="80"> )
Proyecto creado en el framework **Django**, que obtiene data de la API pública citybik - Bike Santiago (https://api.citybik.es/v2/networks/bikerio) con la biblioteca de Python **requests**, y la guarda en una base de datos de **postgreSQL** y la muestra en el navegador a través de una tabla.

# Web scraping - SNIFA (<img src="https://user-images.githubusercontent.com/66185308/219544687-7a92774b-c2bc-48cc-b9ff-efda4e7bf22a.png" width="80"> + <img src="https://user-images.githubusercontent.com/66185308/219544998-7c87fa3b-10e0-4ec1-bbf3-fdc52473a03d.png" width="80">  +  <img src="https://user-images.githubusercontent.com/66185308/219648943-7c47db95-aecb-443f-a6ed-48da61e863e8.png" width="120"> )
Proyecto creado en el framework **Django**, que realiza un web scraping a través de **Selenium** de la página del SNIFA (https://snifa.sma.gob.cl/Sancionatorio/Resultado) para extraer datos de la tabla. Los datos son convertidos en un json y se guardan en un modelo de base de datos de **postgreSQL**, los cuales son visualizados a través de una tabla en el navegador.



## :gear: Requerimientos
- Django
- PostgreSQL/psycopg2
- Requests
- Selenium
- Webdriver-manager

## :memo: Instrucciones

- **Clonar repositorio**:

  ```
  git clone https://github.com/VictoriaBorquez/APIbike-webScraping.git
  ```

- **Entorno virtual**:
  ```
  python -m venv venv
  ```
  ```
  source venv/bin/activate
  ```
  
 
- **Instalar requerimientos**:

  ```
  pip install -r requirements.txt
  ```

- **Crear BD y usuario en PostgreSQL**
  ```
  chmod +x create_db.sh
  ```
  ```
  ./create_db.sh
  ```
  
  
- **Migraciones:**
  ```
  python manage.py makemigrations
  python manage.py migrate
  ```

- **Run project (dentro de directorio /test):** 
  ```
  python manage.py runserver
  ```
  Abrir navegador: 
  - Ruta admin:
    http://127.0.0.1:8000/admin/
    
    Credenciales:
    
      usuario: admin

      password: admin
    
  - Rutas API Bike:
    Muestra tabla con datos estaciones.
    http://127.0.0.1:8000/bike/
    
  - Rutas SNIFA
    1) JSON con datos de página snifa
    http://127.0.0.1:8000/snifa/data
    2) Tabla con datos de página snifa.
    http://127.0.0.1:8000/snifa/
    

