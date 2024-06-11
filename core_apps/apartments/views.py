from typing import Any
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from core_apps.commons.renderers import GenericJSONRenderer
from core_apps.profiles.models import Profile
from .models import Apartment
from .serializers import ApartmentSerializer


class ApartmentCreateAPIView(generics.CreateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    renderer_classes = [GenericJSONRenderer]
    object_label = "apartment"

    def create(self, request: Request, *arg: Any, **kwargs: Any):
        user = request.user
        # aqui verifica-se se é um staff se caso for tem permissão,
        # caso contrario ele verifica se existe um profile e se nesse profile a ocupação é TENANT
        if user.is_superuser or (hasattr(user, 'profile') and user.profile.occupation == Profile.Occupation.TENANT):
            return super().create(request, *arg, **kwargs)
        else:
            return Response({'message': 'You are not allowed to create an apartment, you are a not a tenant'}, status=status.HTTP_403_FORBIDDEN)


class ApartmentDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ApartmentSerializer
    renderer_classes = [GenericJSONRenderer]
    object_label = 'apartment'
