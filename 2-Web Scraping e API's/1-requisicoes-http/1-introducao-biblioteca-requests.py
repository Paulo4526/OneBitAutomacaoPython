#Para fazer requests com python precisamos instalar a biblioteca requests com o comando "pip install requests" no terminal
import requests as req

#1 - Obtendo a versão e métodos da biblioteca
print(req.__version__) #Obtendo a versão
print(dir(req)) #Quais metodos podemos utilizar com a biblioteca

#2 - Requisição get
cep= '08598392'
link = f'http://viacep.com.br/ws/{cep}/json/' #Link da api que feremos a requisição

requisicao = req.get(link)
print('-----------------------------------------------------------------')
print(requisicao) #Retorna a response com o valor do status
print('\n-----------------------------------------------------------------')
print(requisicao.status_code) #Retorna somente o status
print('\n-----------------------------------------------------------------')
print(requisicao.content) #Retorna o corpo da resposta com os valores em bytes string
print('\n-----------------------------------------------------------------')
print(requisicao.text) #Retorna o valor da requisição somente em string
print('\n-----------------------------------------------------------------')