## AgroSYS

<h3>Sistema de impressão de dados<h3>
 
### Ferramentas usadas no projeto
 1. Python
 2. Django
 3. sqlite
 4. Jquery
 5. HTML+CSS
 
 ### INSTRUÇÕES
 
 0. Tenha o pyhton e pip instalado.
 
 1. Use o comando no seu ambiente virutal dentro do projeto
 ```pip install -r requirements.txt``` 
 ele vai instalar as dependências do projeto no seu ambiente virtual.
 
 2. Faça o comando ```python manage.py makemigrations``` e depois ```python manage.py makemigrations```
 para atualizar as tabelas caso seja necessário.
 
 3. Agora para iniciar o seu servidor local com a aplicação use ```py manage.py runserver```
 
 4. após iniciar o servidor entre no link : http://127.0.0.1:8000/logiq (essa é rota padrão para a pagina inicial "localhost:porta/logiq")
 
 5. Agora se ocorreu tudo bem você esta na pagina inicial da aplicação.
 
 6. Na pagina inicial você pode Ver o documento (Detailview), e ou clicar no botão imprimir onde você vai escolher a impressão com ou sem as precauções.
 
 7. Você pode entrar na página do Admin clicando no botão "Admin", irá pedir um usuario e senha, use "admin" nos dois campos. Agora você pode fazer as alterações nas tabelas do banco de dados usando a interface Jazzmin do django.

 ## Diagrama ER
 ![alt text](ER.png)
 
 
