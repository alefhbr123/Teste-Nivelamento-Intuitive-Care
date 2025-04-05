import requests
from bs4 import BeautifulSoup
import zipfile
import os

url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

pdf_links = [a['href'] for a in soup.find_all("a", href=True) if ".pdf" in a['href']]
print("Links encontrados:", pdf_links)

def baixar_pdf(url, nome_arquivo):
    r = requests.get(url)
    with open(nome_arquivo, "wb") as f:
        f.write(r.content)
    print(f"{nome_arquivo} salvo com sucesso.")

baixar_pdf(pdf_links[0], "anexo1.pdf")
baixar_pdf(pdf_links[1], "anexo2.pdf")


with zipfile.ZipFile("anexos.zip", "w") as zipf:
    zipf.write("anexo1.pdf")
    zipf.write("anexo2.pdf")
print("Arquivos compactados em anexos.zip.")