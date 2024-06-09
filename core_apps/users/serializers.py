from django.contrib.auth import get_user_model
from django_countries.serializer_fields import CountryField
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserSerializer
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

User = get_user_model()


class UserCreateSerializer(BaseUserCreateSerializer):
    re_password = serializers.CharField(write_only=True)

    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields = ["id", "username", "first_name", "last_name", "email", "password", "re_password"]

    def validate(self, attrs):
        if attrs['password'] != attrs['re_password']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('re_password')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        return user


# ao fazer authentication com google são esses campos que irão retornar
class CustomUserSerializer(UserSerializer):
    # o source='get_full_name' vem la no model a @property
    full_name = serializers.ReadOnlyField(source='get_full_name')
    gender = serializers.ReadOnlyField(source="profile.gender")
    slug = serializers.ReadOnlyField(source="profile.slug")
    occupation = serializers.ReadOnlyField(source="profile.occupation")
    phone_number = PhoneNumberField(source="profile.phone_number")
    country = CountryField(source="profile.country_of_origin")
    city = serializers.ReadOnlyField(source="profile.city_of_origin")
    avatar = serializers.ReadOnlyField(source="profile.avatar.url")
    reputation = serializers.ReadOnlyField(source="profile.reputation")

    class Meta(UserSerializer.Meta):
        model = User
        fields = [
            "id", "email", "first_name", "last_name", "username", "slug", "full_name", "gender",
            "occupation", "phone_number", "country", "city", "reputation", "avatar", "date_joined"
        ]
        read_only_fields = ["id", "email", "date_joined"]
