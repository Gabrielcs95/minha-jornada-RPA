from selenium import webdriver
from selenium.webdriver.common.by import By
import time as time
import pandas as pd
from pathlib import Path


#criando o navegador
navegador = webdriver.Chrome()

#acessando o site
ROOT_DIR = Path(__file__).resolve().parents[1]
navegador.get('https://rpachallenge.com/')

dataframe = pd.read_excel(ROOT_DIR / "data" / "input" / "challenge.xlsx")


for index, row in dataframe.iterrows():
    # acessa os valores da linha
    # Exemplo: nome = row['Nome'], email = row['Email']
    firstName = row['First Name']
    lastName = row['Last Name']
    companyName = row['Company Name']
    roleCompany = row['Role In Company']
    Address = row['Address']
    email = row['Email']
    phoneNumber = row['Phone Number']

    # Preencher os campos do formulário usando Selenium

    navegador.find_element(By.XPATH, "//input[@ng-reflect-name='labelFirstName']").send_keys(firstName)

    navegador.find_element(By.XPATH, "//input[@ng-reflect-name='labelLastName']").send_keys(lastName)

    navegador.find_element(By.XPATH, "//input[@ng-reflect-name='labelCompanyName']").send_keys(companyName)

    navegador.find_element(By.XPATH, "//input[@ng-reflect-name='labelRole']").send_keys(roleCompany)

    navegador.find_element(By.XPATH, "//input[@ng-reflect-name='labelAddress']").send_keys(Address)

    navegador.find_element(By.XPATH, "//input[@ng-reflect-name='labelEmail']").send_keys(email)

    navegador.find_element(By.XPATH, "//input[@ng-reflect-name='labelPhone']").send_keys(phoneNumber)

    navegador.find_element(By.XPATH, "/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/font/font/input").click()

    






    
