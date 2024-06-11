from rest_framework import serializers
from .models import Apartment


class ApartmentSerializer(serializers.ModelSerializer):
    # ele é incluido no serializador mas não fica exposto
    tenant = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Apartment
        exclude = ["pkid", "updated_at"]
