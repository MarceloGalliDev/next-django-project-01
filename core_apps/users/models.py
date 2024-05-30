import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.utils.translation import gettext_lazy as _
from core_apps.users.managers import UserManager


# instanciando classe de validação de username por expressões regulares
class UsernameValidator(validators.RegexValidator):
    regex = r"^[\w.@+-]+\Z"
    message = _(
        "Your username is not valid. A username can only contain letters, number, a dot, @ symbol, + symbol, and a hyphen"
    )
    flag = 0


class User(AbstractUser):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(max_length=60, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=60, verbose_name=_("Last Name"))
    # db_index é usado para criar o index no banco de dados, facilitando a busca desse dado
    email = models.EmailField(verbose_name=_("Email"), unique=True, db_index=True)
    username = models.CharField(max_length=60, verbose_name=_("Username"), unique=True, validators=[UsernameValidator])

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "first_name", "last_name"]

    # usando o Custom Manager para criar o usuario e persisti-lo no banco de dados
    objects = UserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ["-date_joined"]

    @property
    def get_full_name(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()
