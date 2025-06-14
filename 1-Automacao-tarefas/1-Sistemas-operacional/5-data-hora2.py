from pathlib import Path
from datetime import datetime

root_dir = Path('files')

for path in root_dir.glob('**/*'):
    if path.is_file():
        status = path.stat().st_ctime
        day_created = datetime.fromtimestamp(status).strftime('%d/%m/%Y %H:%M:%S')
        print(day_created)
        #Caso queira agora podemos refazer o path com a data e hora e renomear o arquivo como vimos no arquivo 3 rename
        #Para aprendizado de iteração e visualização pararemos por aqui, porém, fica ao nosso critério agregar o conhecimento com outros metodos