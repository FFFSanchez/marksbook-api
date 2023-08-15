from bookmarks.models import Collection, Bookmark
from .models import MyUser
from .serializers import CollectionSerializer, BookmarkSerializer
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .tools.og_parse import get_og_info


import requests

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile


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
        page_og_info = get_og_info(self.request.data.get("link"))
        # print(page_og_info)
        serializer.save(
            author=self.request.user,
            title=page_og_info.get('og_title'),
            description=page_og_info.get('og_description'),
            type_of_link=page_og_info.get('og_link_type'),
            image_url=page_og_info.get('og_image'),
        )
