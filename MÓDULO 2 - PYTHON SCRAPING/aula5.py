from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
import sqlite3

class Product:
    def __init__(self, id, name, price):
        self.__id= id
        self.__name= name
        self.__price= price
    def get_id(self):
        return self.__id
    def set_name(self, name):
        self.__name= name
    def get_name(self):
        return self.__name
    def set_price(self, price):
        self.__price= price
    def get_price(self):
        return self.__price
    
def login():    
    driver.get("http://localhost:8000/ocomon-4.0RC1/login.php")    
    driver.find_element(By.ID,"user").send_keys("admin")
    driver.find_element(By.ID,"pass").send_keys("admin")
    driver.find_element(By.ID,"bt_login").click(); sleep(2)
    buscar_chamados()
    
def buscar_chamados():
    driver.find_element(By.ID,"OCOMON").click(); sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[1]/nav/div/div/div[1]/div/ul/li[5]/a/i").click();sleep(1)
    frame = driver.find_element(By.ID,"iframeMain")
    driver.switch_to.frame(frame)
    
    driver.find_element(By.XPATH,"/html/body/div[2]/form/div[1]/div[1]/div/div[2]/div/input").click();sleep(1)
    driver.find_element(By.ID,"data_abertura_from").send_keys("01/01/2020");sleep(1)
    driver.find_element(By.ID,"idSearch").click();sleep(3)
    
    tabela = driver.find_element(By.ID,"table_tickets_queue")
    conteudo = tabela.get_attribute("outerHTML")
    soup = BeautifulSoup(conteudo,"html.parser")
    ocorrencias = soup.find(name="table")

    data_frame = pd.read_html(str(ocorrencias))[0]
    data_frame.to_csv("ocorrencias.csv", sep=";",index=False)
    
if __name__ == "__main__":
    login()
    sleep(60)
    driver.quit()
    