from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv
import time
import random

# Opções headless (sem abrir janela visivelmente)
options = webdriver.ChromeOptions()
options.add_argument("--headless")          # Chrome
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
# options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)      # ou webdriver.Firefox(options=options)
wait = WebDriverWait(driver, 10)                 # Espera até 10 segundos

URL = 'https://unirp.edu.br/Curso/1/2'   # Troque pelo URL que você quer scraptar
driver.get(URL)

#print(driver.page_source)  # Imprime o conteúdo da página para verificar se carregou

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

#print(soup.prettify())  # Imprime o HTML formatado para facilitar a leitura
#with open("cursos/direito.html", "w", encoding="utf-8") as f:
#    f.write(soup.prettify())

nome_curso = soup.select_one('div.fonte-destaque').get_text(strip=True)
titulos = soup.select('div.fonte-titulo-3')
print(titulos)
ctd_titulos = soup.select('itemPesquisa')
print(ctd_titulos)

produtos = []
titulos = soup.select('div.fonte-titulo-3')
for titulo in titulos:
    nome = titulo.get_text(strip=True)
    #texto = titulo.select_one('itemPesquisa').get_text(strip=True)
    #link = card.find('a')['href'] if card.find('a') else None
    produtos.append({
        'titulo': "## " + nome
#        'texto': texto
    })

with open("cursos/direito.md", "w", encoding="utf-8") as f:
    for prod in produtos:
        f.write(prod['titulo'] + "\n")
 #       f.write(prod['texto'] + "\n\n")


driver.quit()
