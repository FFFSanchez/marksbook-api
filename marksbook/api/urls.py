from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CollectionViewSet, BookmarkViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'collections', CollectionViewSet, basename='collections')
router.register(r'bookmarks', BookmarkViewSet, basename='bookmarks')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]


# router.register(
#     r'^posts/(?P<post_id>\d+)/comments',
#     CommentViewSet,
#     basename='comment'
# )
