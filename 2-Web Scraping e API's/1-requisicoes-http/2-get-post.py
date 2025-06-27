import requests as req

#1 - Utilizando o link do Json Place Holder uma api publica
url = 'https://jsonplaceholder.typicode.com/posts/2'

#2 - Requisição com Get
response = req.get(url)
print(response)

#3 - Tratando a resposta
if response.status_code == 200:
    print('Requisição realizada com sucesso!')
    print(f'Conteudo da requisição: \n{response.text}')
else:
    print(f'Requisição não foi processada corretamente, verifique os dados se estão corretos e tente novamente. \nStatusCode: {response.status_code}')

#4 - Salvando o conteúdo da resposta como um json
response_json = response.json() #Convertendo a string para json
print(f'Id do Usuario: {response_json['userId']} \nTítulo: {response_json['title']} \nConteúdo: {response_json['body']}')

#5 - Adicionando PayLoad
payload = {
    "id" : {1, 2, 3, 4, 5}, #Recuperando 5 posts de um único usuário
    "userId": 1 #Informando o id do usuário que queremos consultar os posts
}

#6 - Realizando requisição com o playload
get_post_response = req()
