#instalando o yahoo finance comando 'pip install yfinance' para consultas do mercado financeiro
#Instalando matplotlib para graficos 'pip install matplotlib'
import yfinance as yf
from datetime import datetime
from matplotlib import pyplot as plt

end_data = datetime.now().strftime('%Y-%m-%d')
print(end_data)
bb = yf.Ticker('BBAS3.SA')
data_bb = bb.history(
    start = '2020-07-20',
    end = end_data
)

data_bb['Close'].plot()
plt.savefig('bb-preco.png') #Criando a imagem no nosso diretório padrão