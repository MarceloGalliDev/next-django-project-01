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