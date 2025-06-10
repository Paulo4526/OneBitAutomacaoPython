from pathlib import Path

root_dir = Path('files')
# file_path = root_dir.iterdir()
# for path in file_path:
#     print(f'\nPasta: {path.name}')
#     print(f"Arquivos:")
#     for data in path.iterdir():
#         print(f"{data}")

file_path2 = root_dir.glob('**/*')
for path in file_path2:
    if path.is_file():
        parent_folder = path.parts[-2]
        new_file_name = f'{parent_folder}-{path.name}' #Adicionando o nome da pasta ao arquivo
        new_file_path = path.with_name(new_file_name)
        path.rename(new_file_path)