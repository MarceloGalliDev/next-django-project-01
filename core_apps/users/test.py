import pytest
from core_apps.users.serializers import UserCreateSerializer


@pytest.mark.django_db
def test_user_create_serializer():
    data = {
        'email': 'user@example.com',
        'username': 'user',
        'first_name': 'First',
        'last_name': 'Last',
        'password': 'password123',
        're_password': 'password123',
    }

    serializer = UserCreateSerializer(data=data)
    assert serializer.is_valid(), serializer.errors
    user = serializer.save()
    assert user.email == data['email']
    assert user.username == data['username']
    assert user.first_name == data['first_name']
    assert user.last_name == data['last_name']
    assert user.check_password(data['password'])
