# next-django-project-01
 
### Packages
argon2-cffi = para gerar hashes de senhas modernas </br>
djose = sistema de autenticação </br>
django-celery-email = assincronismo no envio de emails


### Commands
Para criar pasta de requirements
```
mkdir -p requirements && touch requirements/{base,local,production}.txt
```

Para criar pasta de settings
```
mkdir -p settings && touch settings/{__init__,base,local,production}.txt
```

Para gerar hashes de SECRET_KEY
```
python -c "import secrets; print(secrets.token_urlsafe(38))"
```


### Logging
Level logging = São as camadas de logging, debug, info, warn, error, critical
Handler logging = São os veículos de entrega do log, podendo ser um arquivo, um email ou console.
Filter logging = São os filtros incluidos para filtrar os logs entre, autorizações entre outros casos.
Formatting log = É a formatação da mensagem, como ela vai parecer.

O uso do %(name)-12s, representa o nome do log e limitando-o a 12 caracteres, os caracteres indicado na frente do %() correseponde ao formato do dado


### Docker
[Document Docker Multi-Stage](https://docs.docker.com/build/building/multi-stage/)

Criando uma rede nova
```
docker network create estate_prod_nw
```


### Passo a Passo
1. Configuramos todo back-end.
2. Configuramos o Docker
3. Criamos o managers.py do app user, para criar o login e authentication
4. Criamos o models.py
5. Criamos o forms.py para uso no admin
6. Criamos o admin.py
7. Iniciamos o projeto do front-end
8. Configuramos o docker do front-end
9. Configurando NGINX
10. Trocar as portas do arquivo local.yml para expose
11. Verficar se foi criado os logs no container
12. Configurando Celery
13. Configurando docker celery
14. Configuramos o cloudinary
15. Criamos o models de profile
16. Criamos signals de profile
17. Configuramos os cookies
18. Criamos cookie_auth.py
19. Configuramos o Jozer para autenticação
20. Configuramos o simple_jwt