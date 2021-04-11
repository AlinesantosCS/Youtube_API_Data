from youtube import YoutubeEstatisticas
 
youTubeApiKey= 'AIzaSyCUId-ShvQYdHzDmLe-hj-IUaR7I6eVktg'
# URL canal curso em video
canal_id = "UCrWvhVmt0Qac3HgsjQK62FQ"
# Classe utiliza os parâmetros do init(chave_api,canal_id) - POO = objeto = atributo
yt = YoutubeEstatisticas(youTubeApiKey,canal_id)
# Chama o objeto yt e armazena os valores nas variáveis da url do pegar_canal_estatisticas() - POO = objeto.atributo
dados =yt.pegar_canal_estatisticas()
# print(dados)
yt.criar_arquivo_json()



