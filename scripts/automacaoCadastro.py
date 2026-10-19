from selenium import webdriver
from selenium.webdriver.common.by import By
import time as time


nav = webdriver.Chrome()

nav.get('https://form.jotform.com/261880094185059')


lista_de_clientes = [
    {
        'nome': 'gabriel',
        'sobrenome': 'silva',
        'email': 'gabriel.silva@example.com',
        'telefone': '1234567890',
        'endereco': 'Rua Exemplo, 123',
        'complemento': 'Apto 101',
        'cidade': 'São Paulo',
        'estado': 'SP',
        'cep': '01234-567',
        'estado civil': 'casado'
    },
    {
        'nome': 'ana',
        'sobrenome': 'souza',
        'email': 'ana.souza@example.com',
        'telefone': '1234567899',
        'endereco': 'Rua vital de negrados, 556',
        'complemento': 'Apto 202',
        'cidade': 'Rio de Janeiro',
        'estado': 'RJ',
        'cep': '98765-432', 
        'estado civil': 'viuvo'
    }, 
    {
        'nome': 'luiz',
        'sobrenome': 'santos',
        'email': 'luiz.santos@example.com',
        'telefone': '1234567898',
        'endereco': 'Rua brasilandia soares, 123',
        'complemento': 'Apto 500',
        'cidade': 'Recife',
        'estado': 'PE',
        'cep': '54321-987',     
        'estado civil': 'solteiro'
    },
    {
        'nome': 'gustavo',
        'sobrenome': 'cabral',
        'email': 'gustavo.cabral@example.com',
        'telefone': '1234567897',
        'endereco': 'Rua camaçari silveira, 555',
        'complemento': 'Apto 600',
        'cidade': 'Salvador',
        'estado': 'BA',
        'cep': '67890-123',
        'estado civil': 'divorciado'
    },
    {
        'nome': 'carla',
        'sobrenome': 'rodrigues',
        'email': 'carla.rodrigues@example.com',
        'telefone': '1234567896',
        'endereco': 'rua quintino bocaiuva, 324',
        'complemento': 'Apto 232',
        'cidade': 'manaus',
        'estado': 'AM',
        'cep': '69000-000',
        'estado civil': 'casado'
    }

]

for clientes in lista_de_clientes:
    time.sleep(5)
    nome_cliente = clientes['nome']
    sobrenome_cliente = clientes['sobrenome']
    email_cliente = clientes['email']
    telefone_cliente = clientes['telefone']
    endereco_cliente = clientes['endereco']
    complemento_cliente = clientes['complemento']
    cidade_cliente = clientes['cidade']
    estado_cliente = clientes['estado']
    cep_cliente = clientes['cep']
    estado_civil_cliente = clientes['estado civil']

    # Preencher os campos do formulário
    nav.find_element(By.ID, 'first_3').send_keys(nome_cliente)
    nav.find_element(By.ID, 'last_3').send_keys(sobrenome_cliente)
    nav.find_element(By.ID, 'input_4').send_keys(email_cliente)
    nav.find_element(By.ID, 'input_5_full').send_keys(telefone_cliente)
    nav.find_element(By.ID, 'input_8_addr_line1').send_keys(endereco_cliente)
    nav.find_element(By.ID, 'input_8_addr_line2').send_keys(complemento_cliente)
    nav.find_element(By.ID, 'input_8_city').send_keys(cidade_cliente)
    nav.find_element(By.ID, 'input_8_state').send_keys(estado_cliente)
    nav.find_element(By.ID, 'input_8_postal').send_keys(cep_cliente)
    xpath_estado_civil = f"//input[@type='radio' and @value='{estado_civil_cliente}']"
    botao_radio = nav.find_element(By.XPATH, xpath_estado_civil)
    nav.execute_script("arguments[0].click();", botao_radio)

    # 2. Clicar no botão de Enviar forçado via JS
    botao_enviar = nav.find_element(By.ID, 'input_2')
    nav.execute_script("arguments[0].click();", botao_enviar)  

    #tempo de espera
    time.sleep(3)   

    #volta a página do formulário
    nav.get('https://form.jotform.com/261880094185059')
    
    #tempo espera
    time.sleep(2)


    







 
