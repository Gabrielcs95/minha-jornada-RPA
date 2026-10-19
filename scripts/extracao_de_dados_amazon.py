from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT_DIR / "data" / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def criar_navegador():

#criando o navegador
 nav = webdriver.Chrome()
 
 return nav

def pesquisar_produtos(nav,product ):
    #acessando o site
    nav.get('https://www.amazon.com.br/')
    
     # Espera ate o elemento existir na tela
    wait = WebDriverWait(nav, 10)
    barra_de_pesquisa = wait.until(EC.presence_of_element_located((By.ID, 'twotabsearchtextbox')))
    barra_de_pesquisa.send_keys(product, Keys.ENTER)
    


def extrair_produtos(nav):

    #localizar a lista com os itens no inspecionar do site
    wait = WebDriverWait(nav, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.sg-col-4-of-4 ')))
    listaProdutos = nav.find_elements(By.CSS_SELECTOR, '.sg-col-4-of-4 ')

    nomeProduto = []
    precoProduto =[]
    urlProduto = []



# for para percorrer todos os itens relacionados ao item pesquisado e salva em lista
    for produtos in listaProdutos:

        try:

            url = produtos.find_element(By.CLASS_NAME,'a-link-normal').get_attribute('href')
            nome = produtos.find_element(By.CLASS_NAME, 'a-text-normal').text

            urlProduto.append(url)
            nomeProduto.append(nome)

            try:
                preco = produtos.find_element(By.CLASS_NAME, 'a-price').text
                precoProduto.append(preco)
        
            except:
                precoProduto.append('Sem preço')
        
        except Exception:
    
            continue

    
    return  urlProduto, nomeProduto, precoProduto

def salvar_excel(urlProduto, nomeProduto, precoProduto, produto):

    #criando o arquivo excel com o ExcelWriter e o mecanismo 'xlsxwriter' 
    ordemList = pd.ExcelWriter(
        OUTPUT_DIR / f'lista_{produto.replace(" ", "_")}.xlsx',
        engine='xlsxwriter',
    )

    #criando o dataframe com as colunas que eu quero
    dataFrame = pd.DataFrame({
    'nomeProduto': nomeProduto,
    'precoProduto': precoProduto,
    'urlProduto': urlProduto
    })

    #passand o data frame pro excel.
    dataFrame.to_excel(ordemList, index=False,  sheet_name='Sheet1')

    #salvando o arquivo excel
    ordemList.close()

def main():
    print("*** ===== PROJETO EXTRAÇÃO DE DADOS ===== ***")
    produto = input("Qual produto você deseja pesquisar? ")

    nav = criar_navegador()
    
    # criando o Bloco try/finally para garantir o fechamento do navegador
    try:
        pesquisar_produtos(nav, produto)
        url, nome, preco = extrair_produtos(nav) 
        
        # Fazendo a  Validação de segurança, pra salva se encontrar produto
        if not nome: 
            print(f"\n  Atenção: Nenhum produto encontrado para a busca '{produto}'.")
        else:
            salvar_excel(url, nome, preco, produto)
            
    except Exception as e:
        print(f"\n Erro inesperado durante a execução: {e}")
        
    finally:
        print("\n  Finalizando o processo e fechando o navegador...")
        nav.quit()

if __name__ == '__main__':
    main()
