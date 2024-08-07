from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import undetected_chromedriver as uc

website = 'https://www.habitaclia.com/alquiler-sabadell-0.htm'           # Página inicial para comenzar

driver = uc.Chrome()
driver.get(website)
driver.find_element("xpath", '//*[@id="didomi-notice-agree-button"]').click()        # Hacemos clic en el botón de aceptación de cookies

driver.maximize_window()
time.sleep(10)

links = []  # Creamos una lista

for i in range(0, 2):                  #  SEGUN cantidad de paginas diponibles en la web en este momento. Por ejemplo en este caso habia dos paginas de alquiler en Sabadell
    website = f'https://www.habitaclia.com/alquiler-sabadell-{i}.htm'
    driver.get(website)
    time.sleep(10)                     # Espera a que la página se cargue

    height = driver.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight );")
    for e in range(0, height, 700):
        driver.execute_script('window.scrollTo(0, {});'.format(e))        # Código para desplazarse por la página de principio a fin
        time.sleep(0.6)

    enlase = driver.find_elements(By.XPATH, '//article[contains(@class, "js-item-with-link") and contains(@class, "gtmproductclick")]')      # Encontramos enlaces a cada objeto en la página

    for element in enlase:  # El atributo data-href contiene el enlace
        link = element.get_attribute('data-href')
        if 'sabadell' in link:
            links.append(link)

data = []  # Creamos una lista para almacenar datos de cada enlace

for link in links:         # Recorremos cada enlace (ciclo)
    driver.get(link)
    time.sleep(2)          # Damos tiempo para que la página se cargue

    height = driver.execute_script(
        "return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight );")
    for e in range(0, height, 700):  # Desplazamos la página de principio a fin
        driver.execute_script('window.scrollTo(0, {});'.format(e))
        time.sleep(0.6)

    price_element = driver.find_element(By.XPATH, '//span[@itemprop="price"]')                  # Precio
    price = price_element.text

    descrip = driver.find_element(By.XPATH, '//h1').text  # Descripción
    agency = driver.find_element(By.CLASS_NAME, 'title').text  # Agencia
    features = driver.find_elements(By.XPATH, '//li[@class="feature"]/strong')                   # Buscamos datos en el tag li, y debajo varios tags strong

    # Obtener texto del primer y tercer elemento
    met = features[1].text if len(features) > 2 else None                                       # Indexación de estos tags strong
    hab = features[2].text if len(features) > 3 else None
    ban = features[3].text if len(features) > 4 else None

    data.append({
        'Descripcion': descrip,
        'Precio': price,
        'M2': met,
        'Hab': hab,
        'baños': ban,
        'Agencia': agency,
        'Enlase': link
    })

df = pd.DataFrame(data)

df.to_excel('C:\\Users\\elena\\OneDrive\\Escritorio\\habitaclia.xlsx', index=False)  # descargaremos los datos q hemos sacado a excel

time.sleep(15)

driver.close()   # cerramos la pestaña
driver.quit()    # cierra el browser
