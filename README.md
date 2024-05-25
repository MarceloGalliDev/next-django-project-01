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