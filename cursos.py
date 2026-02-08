import scraping_unirp as unirp
import scraping_matriz as matriz

link_cursos = [
["https://unirp.edu.br/Curso/274/6","https://unirp.edu.br/Matriz/274/6/1"],
["https://unirp.edu.br/Curso/3/2","https://unirp.edu.br/Matriz/3/2/1"],
["https://unirp.edu.br/Curso/37/2","https://unirp.edu.br/Matriz/37/2/1"],
["https://unirp.edu.br/Curso/44/2","https://unirp.edu.br/Matriz/44/2/1"],
["https://unirp.edu.br/Curso/46/113","https://unirp.edu.br/Matriz/46/113/1"],
["https://unirp.edu.br/Curso/5/2","https://unirp.edu.br/Matriz/5/2/1"],
["https://unirp.edu.br/Curso/50/2","https://unirp.edu.br/Matriz/50/2/1"],
["https://unirp.edu.br/Curso/513/2","https://unirp.edu.br/Matriz/513/2/1"],
["https://unirp.edu.br/Curso/56/2","https://unirp.edu.br/Matriz/56/2/1"],
["https://unirp.edu.br/Curso/8/2","https://unirp.edu.br/Matriz/8/2/1"]]

for link in link_cursos:
    unirp.scrape_unirp(link[0], link[1])
    #matriz.scrape_matriz(link[0], link[1])


