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


produtos = []

# Cada card tem: <div class="produto"> ... <h2>Nome</h2> <span class="preco">R$</span> ...</div>
cards = soup.select('div.fonte-titulo-3')

print(cards)

for card in cards:
    nome = card.get_text(strip=True)
    texto = card.select_one('itemPesquisa').get_text(strip=True)
    #link = card.find('a')['href'] if card.find('a') else None
    produtos.append({
        'nome': "## " + nome,
        'texto': texto
    })

with open("cursos/direito.md", "w", encoding="utf-8") as f:
    for prod in produtos:
        f.write(prod['nome'] + "\n")
        f.write(prod['texto'] + "\n\n")


driver.quit()
