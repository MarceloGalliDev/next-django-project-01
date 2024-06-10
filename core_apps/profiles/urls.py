from django.urls import path
from .views import (AvatarUploadView, ProfileListAPIView, ProfileDetailAPIView, ProfileUpdateAPIView, NonTenantProfileListAPIView)


urlpatterns = [
    path('all/', ProfileListAPIView.as_view(), name='profile_list'),
    path('non-tenant-profiles/', NonTenantProfileListAPIView.as_view(), name='non-tenant-profiles'),
    path('user/my-profile/', ProfileDetailAPIView.as_view(), name='profile_detail'),
    path('user/update/', ProfileUpdateAPIView.as_view(), name='profile_update'),
    path('user/avatar/', AvatarUploadView.as_view(), name='avatar_upload'),
]
