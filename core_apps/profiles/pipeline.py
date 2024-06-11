import cloudinary.uploader

from core_apps.profiles.models import Profile


def save_profile(backend, user, response, *args, **kwargs):
    # aqui verificamos se o backend de autenticação é o google oauth2
    if backend.name == 'google-oauth2':
        # obtemos a resposta aqui vindo do google
        avatar_url = response.get('picture', None)
        if avatar_url:
            # se existir o indice picture ele salva no cloudinary
            upload_result = cloudinary.uploader.upload(avatar_url)
            # inseri no profile o avatar
            profile, created = Profile.objects.get_or_create(user=user)  # pylint: disable=W0612
            # define o campo avatar do perfil com o public_id
            profile.avatar = upload_result['public_id']
            profile.save()
