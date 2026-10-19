# Automações com Python

Coleção de automações desenvolvidas para preenchimento de formulários web, leitura, manipulação e geração de arquivos Excel/Word, além de extração de dados (Web Scraping) utilizando Selenium.

## Estrutura do Projeto

```text
.
├── .vscode/         # Configurações do editor (não versionado)
├── data/
│   ├── input/       # Planilhas e modelos usados localmente (não versionados)
│   │   ├── .gitkeep
│   │   ├── alunosnovos.xlsx
│   │   ├── Certificado1.docx
│   │   └── challenge.xlsx
│   └── output/      # Arquivos gerados pelas automações (não versionados)
├── scripts/         # Automações executáveis (código-fonte)
│   ├── automacaoCadastro.py
│   ├── extracao_de_dados_amazon.py
│   ├── gerador_certificado.py
│   ├── preenchimento_seguro.py
│   ├── tabelas_excel.py
│   ├── testSelenium.py
│   └── todas_as_tabelas.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Requisitos

- Python 3.10 ou superior
- Google Chrome
- ChromeDriver compatível com a versão do Chrome (o Selenium Manager tenta configurar isso automaticamente nas versões atuais do Selenium)

## Instalação

No Windows, abra o terminal na pasta do projeto e execute os comandos abaixo para criar um ambiente virtual e instalar as dependências:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install --upgrade pip
py -m pip install -r requirements.txt
```

## Dados Locais

Os arquivos Excel e Word originais, bem como os gerados, ficam fora do Git (`.gitignore`) para evitar a publicação de dados sensíveis ou pessoais. O arquivo `.gitkeep` garante que a pasta não fique vazia no repositório. Para testar localmente, certifique-se de que os arquivos de entrada estejam nestes caminhos:

| Arquivo | Caminho |
| --- | --- |
| Planilha de alunos | `data/input/alunosnovos.xlsx` |
| Modelo de certificado | `data/input/Certificado1.docx` |
| Planilha do desafio RPA | `data/input/challenge.xlsx` |

Os resultados processados pelos robôs serão gravados automaticamente na pasta `data/output/`.

## Executar Automações

Cada script resolve um problema específico de negócio. Para executar, utilize os comandos abaixo no seu terminal (com o ambiente virtual ativado):

- **Teste de Ambiente:** Script para validar se o Selenium e o navegador estão configurados corretamente.
  ```powershell
  py scripts/testSelenium.py
  ```

- **Geração de Documentos em Massa:** Lê dados de uma planilha e gera certificados Word personalizados.
  ```powershell
  py scripts/gerador_certificado.py
  ```

- **Extração de Dados (Amazon):** Robô que navega no site, extrai detalhes de produtos e compila os resultados em uma planilha.
  ```powershell
  py scripts/extracao_de_dados_amazon.py
  ```

- **Desafio RPA de Cadastro:** Preenche automaticamente formulários web dinâmicos a partir de dados de uma planilha Excel.
  ```powershell
  py scripts/automacaoCadastro.py
  ```

- **Preenchimento de Seguros:** Automação focada em navegação e preenchimento de formulários específicos.
  ```powershell
  py scripts/preenchimento_seguro.py
  ```

- **Manipulação de Excel:** Leitura, edição e consolidação de dados em planilhas.
  ```powershell
  py scripts/tabelas_excel.py
  py scripts/todas_as_tabelas.py
  ```

## Como Publicar no GitHub

Comandos utilizados para versionar e enviar este projeto para o repositório remoto:

```powershell
git init
git add .
git commit -m "Organiza projeto de automações Python e adiciona README"
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
git push -u origin main
```

*Antes do primeiro `git push`, confirme com `git status` se arquivos de dados estão sendo ignorados corretamente.*

## Autor

**Gabriel da Silva Costa**
- LinkedIn: https://LinkedIn.com/in/Gabriel-costa95
- GitHub: https://github.com/Gabrielcs95