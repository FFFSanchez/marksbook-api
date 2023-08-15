from django.urls import path, include

from .views import UserViewSet #, MyUserViewSet
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )
from rest_framework.routers import DefaultRouter


app_name = 'users'


# router = DefaultRouter()
# router.register(r'users', MyUserViewSet, basename='users')


urlpatterns = [
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    # path('v2/', include(router.urls)),
]
