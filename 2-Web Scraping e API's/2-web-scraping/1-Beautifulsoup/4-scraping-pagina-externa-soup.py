#Nesse eemplo utilizaremos a biblioteca requests para recuperar valores web, o comando para instalar a biblioteca é "pip install requests"

from bs4 import BeautifulSoup
import requests as req
import os
import pandas
import time

#1 - Criando a pasta onde salvaremos nossos dados em csv
pasta = 'CSV'
os.makedirs(pasta, exist_ok=True)

#2 - Colentando vagas em Python de um site externo times job(url = https://m.timesjobs.com/)
#Abaixo a url com o resultado das buscas por vagas
url = 'https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=python&cboWorkExp1=-1&txtLocation='
response = req.get(url)
print(response.status_code)
soup = BeautifulSoup(response.text, 'lxml') #Recuperando o valor do resultado e mudando para xml
jobs = soup.find_all('li')
print(len(jobs)) #Mostra quantos valores foram atribuidos a variavel jobs

save_job = []
save_skills = []
save_date = []
save_experience = []


for job in jobs[:10]:
    try:
        job_scope = job.find('h3').find('a').text
        post_date = job.find('h4').find('span', class_='posting-time').text
        exp_time = job.find('div', class_='srp-exp').text
        skills = job.find('a', class_='srphglt').text
        save_skills.append(skills)
        save_job.append(job_scope)
        save_date.append(post_date)
        save_experience.append(exp_time)
        print(f'\nFunção: {job_scope} \nData da postagem: {post_date} \nTempo de Experiencia: {exp_time.split(' ')[0]} à {exp_time.split(' ')[2]} anos \nSkills: {skills}')
    except:
        continue

#3 - Exportando informações para o CSV
python_jobs = pandas.DataFrame()
python_jobs['funcao'] = save_job
python_jobs['tempo_exp'] = save_experience
python_jobs['skill'] = save_skills
python_jobs['data_pub'] = save_date
print(python_jobs)
python_jobs.to_csv(os.path.join(pasta, f'python_jobs_{time.time()}.csv'))