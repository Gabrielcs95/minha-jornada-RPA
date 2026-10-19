from selenium import webdriver
from selenium.webdriver.common.by import By
import time as time
import pandas as pd
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT_DIR / "data" / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

#criando o navegador
nav = webdriver.Chrome()

#acessando o site
nav.get('https://rpachallengeocr.azurewebsites.net/')

i = 1

dados = []
#usando o while para percorrer as 4 paginas da tabela
while i <= 4:

    #pegando a tabela completa
    tabela = nav.find_element(By.XPATH, '//*[@id="tableSandbox"]')

    #acessando todas as linhas
    linhas = tabela.find_elements(By.TAG_NAME, 'tr')

    #percorrendo todas as linhas
    for linha_elem in linhas:
        dados.append(linha_elem.text.split()) #adicionando a uma nova lista
    
    #clicando pra ir a proxima pagina
    nav.find_element(By.XPATH, '//*[@id="tableSandbox_next"]').click()

    time.sleep(5)


    i += 1
#------------------------ parte 2 ---------------------------

#nessa parte 2 sera criado o arquivo excel com o ExcelWriter e o mecanismo 'xlsxwriter'
#cria um arquivo excel com xlsxwriter
ordemList = pd.ExcelWriter(OUTPUT_DIR / 'table.xlsx', engine='xlsxwriter')


#criando o dataframe com as colunas que eu quero
dataFrame = pd.DataFrame(dados, columns=['dados', 'informacoes', 'datas'])

#passand o data frame pro excel.
dataFrame.to_excel(ordemList, index=False, sheet_name='Sheet1')

#salvando o arquivo excel
ordemList.close()


print('Fim do programa')
    



