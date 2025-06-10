from pathlib import Path

root_dir = Path('files/dados')
print(list(root_dir.iterdir())) #Iterando com o diretório para retornar quais arquivos existem dentro da pasta dados
file_path = root_dir.iterdir()
for files in file_path: #Iterando com for
    print(f"Nome do Arquivo: {files.stem} \nDiretório do Arquivo: {files} \nTipo do Arquivo: {files.suffix}\n")
    new_file_name = f'novo-{files.stem}{files.suffix}' #Aqui somente criamos uma prévia de como o arquivo ierá ficar,, porém as alterações ainda não foram feitas.
    print(new_file_name)
    new_file_path = files.with_name(new_file_name) #Criando o préfixo junto ao diretório
    files.rename(new_file_path) #Salvando as alterações feitas