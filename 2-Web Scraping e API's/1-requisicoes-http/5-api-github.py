import requests
import requests as req

#1 - Fazendo uma requisição get para a api do github
url = 'https://api.github.com/events'
response = requests.get(url)
print(f'Statud da Requisição: {response.status_code}')
response_json = response.json()
for i in response_json:
    print(i, '\n')

#2 - Verificando a versão da API
url_version = 'https://api.github.com/versions'
version_response = req.get(url_version)
print(f'Status da Requisição: {version_response.status_code}')
print(f'Versão da API: {version_response.json()}')

#3 - Realizando requisição com a versão especifica
headers = {
    'X-Github-Api-Version': f'{version_response.json()[0]}'
}
url_atualizado = req.get(url, headers=headers)
print(url_atualizado.json())