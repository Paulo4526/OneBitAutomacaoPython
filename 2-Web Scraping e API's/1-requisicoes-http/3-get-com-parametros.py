import requests as req

#1 - Utilizando o link do Json Place Holder uma api publica
url = 'https://jsonplaceholder.typicode.com/posts' #Sem os parametros de id dos posts

#3 - Adicionando PayLoad
payload = {
    "id" : [1, 2, 3, 4, 5], #Recuperando 5 posts de um único usuário
    "userId": 1 #Informando o id do usuário que queremos consultar os posts
}

#3 - Requisição com Get
response = req.get(url, params=payload)
print(response.text)

#4 - Convertendo a resposta em json
response_json = response.json() #Iterando as respostas
for i in response_json:
    print(i, '\n')
