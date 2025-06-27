import requests as req

#1 - Recuperando a versão do github
url_git_version = 'https://api.github.com/versions'
git_request = req.get(url_git_version)
git_json = git_request.json()

#2 - Criando header para introduzir a versão do github
headers = {
    'X-Github-Api-Version': f'{git_json[0]}'
}

#3 - Recuperando informações do usuário git
base_url = 'https://api.github.com'
user = 'OneBitCodeBlog'
user_url = f'{base_url}/users/{user}/repos'
user_request = req.get(user_url, headers=headers)
print(f'Status: {user_request.status_code}')
user_json = user_request.json()
for i in user_json:
    print(i, '\n')