import requests
import json


class YoutubeEstatisticas:
    def __init__(self,chave_api,canal_id):
        self.chave_api = chave_api
        self.canal_id  = canal_id
        self.canal_estatisticas = None

    def pegar_canal_estatisticas(self):
        url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={self.canal_id}&key={self.chave_api}'
        print(url)
        # Exibe as informações em formato JSON
        url_json = requests.get(url)
        print(url_json.history) # Retorna o estado da requisição
        if url_json.status_code == 200:
            print("Status 200 - Requisição foi um sucesso!")
        elif url_json.status_code == 400:
            print("Status 400 - Ocorreu um erro de requisição por parte do cliente!")
        elif url_json.status_code == 400:
            print("Status 404 - Ocorreu um erro de requisição por parte do cliente!")

        
        # Utiliza a biblioteca Json que fornece formas de mostrar o formato json que no caso em texto
        dados = json.loads(url_json.text)
        # print(dados) # Retorna o JSON inteiro

        try:
            # Pega os dados somentes da estatisticas do Json
            """ 
            Pega a chave itens que está na primeira chave selecionando toda a cheve itens 
            em seguida seleciona dentro da chave a chave estatisticas 
            """
            dados = dados['items'][0]['statistics']
        except:
            """
             Se a chave da API não for válida os dados retornam None
            """
            dados = None

        self.canal_estatisticas = dados
        return dados

    def criar_arquivo_json(self):
        #  Se for None vai retornar None do pegar canal estatisticas
        if self.canal_estatisticas is None:
            return
        nome_canal = "Curso em Video" 
        #  Substitui todos espaços em branco em sublinhado do nome do canal
        nome_canal = nome_canal.replace(" ","_").lower()
        # Arquivo será nome do canal + .json
        nome_arquivo = nome_canal + ".json"
        # vai abrir o arquivo e escrever em fomato json as estatisticas do canal
        with open(nome_arquivo,'w') as arquivo:
            json.dump(self.canal_estatisticas, arquivo,indent=4)
        print("Arquivo criado em dump")

""" 
load - Transforma em Json em um objeto Python
dump - Transforma o objeto python em Json
"""


  
    


