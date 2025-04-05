<h1 align="center">Teste Nivelamento Intuitive Care</h1>
Este repositório contém a solução para os testes de nivelamento, divididos em quatro módulos:

- Teste de Web Scraping

- Teste de Transformação de Dados

- Teste de Banco de Dados

- Teste de API

# 1. 📌Teste de Web Scraping
## Objetivo:
Desenvolver um código em Python (ou Java) que acesse um site do governo, faça download de anexos em formato PDF e compacte esses arquivos em um único arquivo (ZIP).

Principais etapas e decisões:

- Acessamos o site da ANS (link) utilizando bibliotecas como requests e BeautifulSoup (ou Selenium, conforme necessidade).

- Realizamos o download dos Anexos I e II em PDF.

- Compactamos os PDFs baixados em um arquivo ZIP utilizando a biblioteca zipfile do Python.

# 2. 📌Teste de Transformação de Dados
## Objetivo:
Extrair dados da tabela "Rol de Procedimentos e Eventos em Saúde" contida em um PDF (Anexo I), transformá-los em uma estrutura tabular e salvar o resultado em um arquivo CSV compactado.

Principais etapas e decisões:

- Utilizamos bibliotecas de extração de dados de PDF, como camelot e tabula-py, para extrair as informações da tabela.

- Realizamos limpeza dos dados, como remoção de linhas vazias, ajuste de colunas, substituição de abreviações (por exemplo, substituindo "OD" por "Seg. Odontológica" e "AMB" por "Seg. Ambulatorial").

- Os dados foram organizados em um DataFrame, reordenados conforme o cabeçalho exigido e exportados para CSV.

- O arquivo CSV foi compactado em um arquivo ZIP com o nome "Teste_Álefh.zip".

# 3. 📌Teste de Banco de Dados
## Objetivo: Estruturar e importar os dados dos arquivos baixados para um banco de dados e realizar análises.

Banco de Dados: Scripts compatíveis com MySQL 8 ou PostgreSQL (>10.0).

## Passos Realizados:

### Preparação dos Dados:

- Download dos arquivos dos últimos 2 anos do repositório de demonstrações contábeis

- Download dos dados cadastrais das operadoras ativas

### Criação das Tabelas:

- Criação de tabelas para armazenar os dados dos demonstrativos contábeis e os cadastros das operadoras.

### Importação dos Dados:

- Utilização de comandos LOAD DATA INFILE (MySQL) ou \copy (PostgreSQL) para importar os dados dos CSVs.

- Tratamento de encoding e delimitadores para garantir a correta importação (ex.: arquivos com delimitador ; e vírgula como separador decimal).

### Análise de Dados:

- Desenvolvimento de queries analíticas para responder:

- Quais as 10 operadoras com maiores despesas em "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO-HOSPITALAR" no último trimestre.

- Quais as 10 operadoras com maiores despesas nessa categoria no último ano.

# 4. 📌Teste de API
## Objetivo: Desenvolver uma interface web que interaja com um servidor em Python para realizar buscas textuais na lista de cadastros das operadoras.

### 🚀Tecnologias Utilizadas:

- Back-end: Python com Flask

- Front-end: Vue.js

### Funcionalidades Implementadas:

#### Servidor API (Flask):

- Carrega os dados dos cadastros das operadoras a partir de um CSV.

- Disponibiliza uma rota /api/operadoras que recebe um parâmetro de consulta (q) e retorna os registros filtrados em formato JSON.

#### Interface Web (Vue.js):

- Um componente Vue que permite ao usuário realizar buscas textuais e exibe os resultados retornados pela API.

# Instruções para Execução
## Back-end (Flask)
### 1. Instalação das Dependências:

- Instale o Flask e outras dependências:

```bash
pip install flask pandas
```

### 2. Executando o Servidor:

- No terminal, execute:

```bash
python server.py
```
O servidor ficará disponível em: [http://127.0.0.1:5000](http://127.0.0.1:5000/api/operadoras).

## Front-end (Vue.js)
- Instalação e Execução:

- Caso esteja utilizando o Vue CLI, clone o repositório, instale as dependências e execute:

```bash
npm install
npm run serve
```
Integre o componente de busca conforme o exemplo em Search.vue.

## 🏗Estrutura do Projeto
```text
├── README.md                 # Este arquivo: documentação e descrição do projeto.
├── Relatorio_cadop.csv       # CSV gerado (relatório) com os dados processados.
├── Teste API                 # Pasta contendo os arquivos relacionados ao teste de API.
│   ├── Search.vue            # Componente Vue.js para realizar buscas na API.
│   └── server.py             # Servidor Python (Flask/FastAPI) que expõe os endpoints da API.
├── Teste_BD.sql              # Scripts SQL para criação de tabelas, importação dos CSVs e execução de queries analíticas.
├── teste_transfDados.py      # Script Python para extração e transformação de dados a partir dos PDFs (e geração do CSV).
└── teste_webscraping.py      # Script Python para realização do web scraping do site da ANS.
```

# Considerações Finais
Este projeto demonstrou a integração de diversas tecnologias e técnicas para a resolução de desafios práticos em web scraping, transformação de dados, manipulação de banco de dados e desenvolvimento de APIs. Ao longo do desenvolvimento, foram superados desafios como a extração de dados de PDFs complexos, a padronização de dados com encoding diferente e a construção de queries analíticas para extrair informações relevantes dos dados contábeis e cadastrais.
