import scraping_unirp as unirp
import scraping_matriz as matriz

link_cursos = [["https://unirp.edu.br/Curso/513/2","https://unirp.edu.br/Matriz/513/2/3"],
               ["https://unirp.edu.br/Curso/1/2","https://unirp.edu.br/Matriz/1/2/1"],
               ["https://unirp.edu.br/Curso/2/2","https://unirp.edu.br/Matriz/2/2/1"]]

for link in link_cursos:
    unirp.scrape_unirp(link[0], link[1])
    #matriz.scrape_matriz(link[0], link[1])


