# pip install selenium

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import urllib.request

def iniciandoChrome():
    driver = webdriver.Chrome(executable_path=r"\chromedriver.exe")
    driver.get("http://selenium.dev")
    driver.quit()

def iniciandoChrome2():
    driver  = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.infomoney.com.br/")
    dados_infomoney = driver.find_element(By.ID, "high").text
    print(dados_infomoney)
    sleep(5)
    driver.quit()

def fundsexplorer():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.fundsexplorer.com.br/funds/rbds11")
    print(f'Nome do FII: {driver.find_element(By.CLASS_NAME, "section-title").text}')
    print(f'Preco: {driver.find_element(By.CLASS_NAME, "price").text}')
    print(f'Variacao do Dia: {driver.find_element(By.XPATH, "/html/body/section/section/div/div/div/div[3]/div/span[2]").text}')
    print(f'DY: {driver.find_element(By.CLASS_NAME, "indicator-value").text}')
    print(f'Ultimo Rendimento: {driver.find_element(By.CLASS_NAME, "indicator-value").text}')
    sleep(5)
    driver.quit()

def exercicio1_2():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://statusinvest.com.br/")
    print(f'Ibovespa: {driver.find_element(By.XPATH, "/html/body/main/section[1]/div[2]/div[2]/a[1]/div[1]/strong").text}')
    print(f'CDI: {driver.find_element(By.XPATH, "/html/body/main/section[1]/div[2]/div[2]/a[2]/div[1]/strong").text}')
    print(f'IPCA: {driver.find_element(By.XPATH, "/html/body/main/section[1]/div[2]/div[2]/a[3]/div[1]/strong").text}')    
    driver.get('https://statusinvest.com.br/acoes/busca-avancada')
    sleep(2)
    driver.find_element(By.XPATH, '/html/body/main/div[3]/div/form/div[1]/div[1]/div/input').click()
    driver.find_element(By.XPATH, '/html/body/main/div[3]/div/form/div[1]/div[1]/div/ul/li[8]').click()
    driver.find_element(By.XPATH, '/html/body/main/div[3]/div/div/div/button[2]').click()
    sleep(2)
    tabela = driver.find_elements(By.CLASS_NAME, 'list')
    print(tabela[0].text)
    sleep(5)

def scraping_image():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.imdb.com/title/tt0406728/?ref_=tt_sims_tt_i_1")
    driver.implicitly_wait(10) #segundos
    div_imagens= driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[2]/div[2]/div[2]')
    imagem = div_imagens.find_elements(By.TAG_NAME, "img")[5]
    src= imagem.get_attribute("src")
    print(src)
    try:
        urllib.request.urlretrieve(src, r"C:\Users\Hideki\Desktop\teste.jpg")
        print("Imagem  copiada")
    except:
        print("Erro")
        
if __name__ == "__main__":
    #iniciandoChrome()
    #iniciandoChrome2()
    #fundsexplorer()
    #exercicio1()
    scraping_image()