from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path

import pandas as pd


ROOT_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT_DIR / "data" / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

bot = webdriver.Chrome()

bot.get('https://rpachallengeocr.azurewebsites.net/')

tabela = bot.find_element(By.XPATH, '//*[@id="tableSandbox"]')

linhas = tabela.find_elements(By.TAG_NAME, 'tr')
colunas = tabela.find_elements(By.TAG_NAME, 'td')

#criar dataframe
list_excel = []

for linha_tabela in linhas:

    list_excel.append(linha_tabela.text.split())


#criando um arquivo excel com xlsxwriter
tabela_organizada = pd.ExcelWriter(
    OUTPUT_DIR / 'newtable.xlsx',
    engine='xlsxwriter',
)


#criando o dataframe com as colunas que eu quero
dataFrame = pd.DataFrame(list_excel, columns=['Dados', 'informacoes', 'registros'])


#pega o dataframe e passa pro excel
#usando o index falso para nao gerar colunas extras
dataFrame.to_excel(tabela_organizada, index=False, sheet_name='Sheet1')

#depois salvar o arquivo com o .save()
tabela_organizada.close()
