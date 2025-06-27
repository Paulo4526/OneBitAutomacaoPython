#Utilizar a biblioteca pandas muito utilizada para análise de dados, instale com o comando "pip install pandas"

import requests as req
import pandas
import os
import time

pasta = 'CSV'
os.makedirs(pasta, exist_ok=True)

#1 - Recuperando a versão do github
url_git_version = 'https://api.github.com/versions'
git_request = req.get(url_git_version)
git_json = git_request.json()

#2 - Autenticação github
#Aqui colocar a variavel acess token
# headers = {
#     'Authorization': 'Bearer ' + access_token,
#     'X-Github-Api-Version': f'{git_json[0]}'
# }

#3 - Recuperando informações do usuário git
base_url = 'https://api.github.com'
user = 'OneBitCodeBlog'
user_url = f'{base_url}/users/{user}/repos?per_page=100&page=1' #Definindo que terá 100 itens por página não necessitando a iteração pela pagina
repo_lis =[]


#4 - Recuperando os dados
user_request = req.get(user_url, headers=headers)
print(len(user_request.json()))
print(f'Status: {user_request.status_code}')
user_json = user_request.json()

#5 - Salvando valores selecionados
for i in user_json:
    try:
        out_put_data = {
            'id': f'{i['id']}',
            'user': f'{i['owner']['login']}',
            'nome_projeto': f'{i['name']}',
            'link_projeto': f'{i['html_url']}'
        }
        repo_lis.append(out_put_data)
    except:
        repo_lis.append(None)

for i in range(0,len(repo_lis)):
    print(f'{repo_lis[i]}')

#6 - Criando o dataframe
dados_obc = pandas.DataFrame() #Instanciando o Pandas Data Frame
dados_obc['user_name'] = [repo['user'] for repo in repo_lis if repo is not None]
dados_obc['repo_name'] = [repo['nome_projeto'] for repo in repo_lis if repo is not None]
dados_obc['repo_link'] = [repo['link_projeto'] for repo in repo_lis if repo is not None]
print(dados_obc)
dados_obc.to_csv(os.path.join(pasta, f'arquivo-gerado-{time.time()}.csv'))