import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from snifa.models import Result



def scrape_data():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


    driver.get("https://snifa.sma.gob.cl/Sancionatorio/Resultado")
    id = driver.find_element(By.ID,"myTable_info")
    max_pages = int(id.text[-5:].replace(",",""))
    data = []
    for page_index in range(1,10): #Change 10 to max_pages+1 
        print("Processing page : ",page_index)
        
        table_id = driver.find_element(By.CLASS_NAME, 'dataTables_wrapper')
        rows = table_id.find_elements(By.TAG_NAME, "tr") 
        for row in rows:
            col = row.find_elements(By.TAG_NAME, "td") 
            if(len(col)>1):
                proceedings=col[1].text
                auditable_unit=col[2].text
                url_auditable_unit=col[2].find_element(By.TAG_NAME, 'a').get_attribute('href')
                name_social_reason=col[3].text
                category=col[4].text
                region=col[5].text
                status=col[6].text
                detail=col[7].find_element(By.TAG_NAME, 'a').get_attribute('href')
                Result.objects.create(
                    proceedings=col[1].text,
                    auditable_unit=col[2].text,
                    url_auditable_unit=col[2].find_element(By.TAG_NAME, 'a').get_attribute('href'),
                    name_social_reason=col[3].text,
                    category=col[4].text,
                    region=col[5].text,
                    status=col[6].text,
                    detail=col[7].find_element(By.TAG_NAME, 'a').get_attribute('href')
                )
                data.append({
                    'Expediente':proceedings, 
                    'Unidad fiscalizable': auditable_unit,
                    'URL Unidad fiscalizable': url_auditable_unit,
                    'Nombre o Razón social':name_social_reason,
                    'Categoría':category,
                    'Región':region,
                    'Estado':status,
                    'Detalle':detail
                    })
        dropdown = driver.find_element(By.ID, "myTable_next")
        dropdown.click()
    json_data = json.dumps(data)
    
    driver.quit()
    return json_data
