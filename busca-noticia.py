# import pandas as pd
from noticia import Noticia
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys


def buscar_noticia(link):
    nav = webdriver.Chrome()
    # Saber os site a serem acessados
    # Esolher o site
    link = link
    nav.get(link)
    elem = nav.find_element(By.XPATH, '/html/body/main/section[1]/div/section[2]/div/article[1]/div/h3/a').get_attribute("innerText")
    elem_link = nav.find_element(By.XPATH, '/html/body/main/section[1]/div/section[2]/div/article[1]/div/h3/a').get_attribute("href")


    parentElement = nav.find_element(By.CLASS_NAME, "sentinel-home-list")
    elementList = parentElement.find_elements(By.TAG_NAME, "div")


    #print(elementList.get_attribute("innerText"))

    #for element in elementList:
        #print(element.get_attribute("innerText"))


    return elem_link

#buscar_noticia('https://gamerant.com/')



#df = pd.read_json('data.json')


#noticia1 = Noticia(f'{elem}', 'descrição 1', f'{elem_link}')
#print(noticia1.get_titulo())
#print(noticia1.get_link())
##print(df.to_string())