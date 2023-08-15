from bookmarks.models import Collection, Bookmark
from .models import MyUser
from .serializers import CollectionSerializer, BookmarkSerializer
from rest_framework import viewsets
from django.shortcuts import get_object_or_404


class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    pagination_class = None
    # permission_classes = [OwnerOrReadOnly]


class BookmarkViewSet(viewsets.ModelViewSet):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    pagination_class = None
    # permission_classes = [OwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

