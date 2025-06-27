import requests as req

#1 - Informando os novos dados no formato json
new_data = {
    'userId': 1,
    'id': 1,
    'title': "Aprendento requisições com Python",
    'body': 'Enviando informações para API com o método POST com a biblioteca requests em Python'
}

#2 - Endpoint da API
url = 'https://jsonplaceholder.typicode.com/posts'

#3 - Enviando dados via metodo post com 2 parametros, url, e os valores
post_response = req.post(
    url,
    json=new_data
)

print(post_response.status_code)
print(post_response.text) #Retorna o conteúdo criado

#4 - Recuperando os valores enviados em json
post_json = post_response.json()
print(post_json)