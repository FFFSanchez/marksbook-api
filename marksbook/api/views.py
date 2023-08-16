from rest_framework import viewsets

from bookmarks.models import Bookmark, Collection

from .permissions import OwnerOrReadOnly
from .serializers import BookmarkSerializer, CollectionSerializer
from .tools.og_parse import get_og_info


class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    pagination_class = None
    permission_classes = [OwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        """ Show to user only his collections """
        return self.request.user.collections.all()


class BookmarkViewSet(viewsets.ModelViewSet):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = [OwnerOrReadOnly]

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

    def get_queryset(self):
        """ Show to user only his bookmarks """
        return self.request.user.bookmarks.all()
