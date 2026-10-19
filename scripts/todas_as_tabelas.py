from selenium import webdriver
from selenium.webdriver.common.by import By
import time as time


nav = webdriver.Chrome()

nav.get('https://rpachallengeocr.azurewebsites.net/')

i = 1

while i < 4:
    tabela = nav.find_element(By.XPATH, '//*[@id="tableSandbox"]')

    linhas = tabela.find_elements(By.TAG_NAME, 'tr')

    for linha_elem in linhas:
        print(linha_elem.text)
    
    nav.find_element(By.XPATH, '//*[@id="tableSandbox_next"]').click()

    time.sleep(5)


    i += 1


print('Fim do programa')
    


