from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BookmarkViewSet, CollectionViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'collections', CollectionViewSet, basename='collections')
router.register(r'bookmarks', BookmarkViewSet, basename='bookmarks')

urlpatterns = [
    path('v1/', include(router.urls), name='apis'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
