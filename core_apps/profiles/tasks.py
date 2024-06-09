# esse arquivo ele é capturado automaticamente pela config do Django, incluida no base.py

from uuid import UUID
from celery import shared_task
import cloudinary.uploader
from .models import Profile


@shared_task(name='upload_avatar_to_cloudinary')
def upload_avatar_to_cloudinary(profile_id: UUID, image_content: bytes) -> None:
    profile = Profile.objects.get(id=profile_id)
    response = cloudinary.uploader.upload(image_content)
    profile.avatar = response['url']
    profile.save()


@shared_task(name='update_all_reputations')
def update_all_reputations():
    for profile in Profile.objects.all():
        # aqui esse update_reputation está vindo do método do models.py de profile
        profile.update_reputation()
        profile.save()


# temos que configurar o Intervals no Periodic Tasks la no acesso admin, para indicar o CronJob
