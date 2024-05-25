from os import getenv, path  # noqa: F401
from dotenv import load_dotenv  # type: ignore
from .base import *  # noqa: F403
from .base import BASE_DIR


local_env_file = path.join(BASE_DIR, ".envs", ".env.local")

if path.isfile(local_env_file):
    load_dotenv(local_env_file)

DEBUG = True

SITE_NAME = getenv("SITE_NAME")

SECRET_KEY = getenv("DJANGO_SECRET_KEY", "PMcqWdmMVC2MocbNqqEhIw9kKBIOQquSV_4EKXSwC9CpJdRabC8")

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0"]
