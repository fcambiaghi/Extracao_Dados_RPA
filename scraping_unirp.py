def scrape_unirp(url_curso, url_matriz):
    import requests
    from bs4 import BeautifulSoup
    import scraping_matriz as matriz

    url = url_curso 
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        conteudo_texto = ''

        # parse usando lxml se você instalou
        soup = BeautifulSoup(response.content, 'lxml')  # ou 'html.parser' (padrão)
        
        nome_curso = soup.select_one('div.fonte-destaque').get_text(strip=True)

        cabecalho_yaml = f'''
---
instituicao: "Centro Universitário de Rio Preto - UNIRP"
complemento chunck: {nome_curso}
tags: [tagsReplace]
---
    '''
        blocos = soup.select('.fonte-12pt-800')   # lista de <div class="fonte-12pt-800">

        result = {}
        for bloco in blocos:
            # Inspeção manual: bloco.contents = [ '\n        Investimento\n        ', div_fonte500_object, '\n   ']
            label_text = bloco.decode_contents().split('<div')[0].strip()   # pega só o texto antes do clique <div>
            
            # 3.2) O valor está em <div class="fonte-500">
            valor_div = bloco.find('div', class_='fonte-500')
            valor_text = valor_div.get_text(strip=True) if valor_div else None
            
            result[label_text] = valor_text

        apresentacao = '# Curso de ' + nome_curso + '\n'
        apresentacao += '**Instituição** Centro Universitário de Rio Preto - UNIRP\n'
        for item in result.items():
            if item[1]:  # evitar valores None
                apresentacao += f'* {item[0]}: {item[1]}\n'

        info_legais = '## Informações Legais\n'
        div_obj = soup.find('div', class_='fonte-10pt-400 fonte-branca sombra-texto')
        info_legais += div_obj.get_text(separator='\n', strip=True)
        
        diferenciais = '## Diferenciais do curso\n'
        blocos = soup.select('div[style*="margin-bottom: 8px;"]')

        for bloco in blocos:
            titulo = bloco.select_one('div.fonte-destaque.fonte-700')
            diferenciais += '**' + titulo.get_text(strip=True) + '**\n' if titulo else ''

            descricao = bloco.select_one('div.alinhamento-justificado')
            diferenciais += descricao.get_text(strip=True) + '\n\n' if descricao else ''
        
        # objetivo e mercado de trabalho
        titles = soup.select('div.fonte-titulo-3')
        ctd_titulos = soup.select('div.itemPesquisa')

        for i in range(2):
            conteudo_texto += f'## {titles[i].get_text(strip=True)}\n'
            conteudo_texto += f'{titles[i].find_next_sibling("div", class_="itemPesquisa").get_text(strip=True)}\n\n'

        texto_matriz = matriz.scrape_matriz(url_matriz)

        conteudo_texto = cabecalho_yaml + '\n' + apresentacao + '\n' + info_legais + '\n\n' + conteudo_texto + diferenciais + '\n' + texto_matriz
        conteudo_texto = conteudo_texto.strip()
        # falta carregar a matriz curricular

        with open(f"cursos/{nome_curso}.md", "w", encoding="utf-8") as f:
            f.write(conteudo_texto)

    else:
        print(f'Erro ao acessar {url}: {response.status_code}')

if __name__ == "__main__":
    scrape_unirp()