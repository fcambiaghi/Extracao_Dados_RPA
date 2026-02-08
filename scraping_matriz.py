def scrape_matriz(url_matriz):
    import requests
    from bs4 import BeautifulSoup

    response = requests.get(url_matriz, timeout=10)

    if response.status_code == 200:
        # parse usando lxml se você instalou
        soup = BeautifulSoup(response.content, 'lxml')  # ou 'html.parser' (padrão)
        periodos = soup.select('fieldset')

        texto_matriz = '## Matriz Curricular\n'
        #nome_curso = soup.get_text(strip=True)
        #with open(f"cursos/MatrizExemplo.md", "w", encoding="utf-8") as f:
        #    f.write(response.text)

        for periodo in periodos:
            #texto_matriz += periodo.get_text(strip = True) + '\n'
            texto_matriz += periodo.select_one('legend').get_text(strip=True) + '\n'
            disciplinas_divs = periodo.find_all('div', class_='marcar')
            for disciplina_div in disciplinas_divs:
                texto_matriz += '- ' + disciplina_div.get_text(strip=True) + '\n'

        return texto_matriz

        #print(texto_matriz)
        #with open(f"cursos/MatrizExemplo.md", "w", encoding="utf-8") as f:
        #    f.write(texto_matriz)

if __name__ == "__main__":
    scrape_matriz()        

        