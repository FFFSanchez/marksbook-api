from bookmarks.models import Collection, Bookmark
from rest_framework import serializers


class BookmarkSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='email',
        read_only=True)
    collection = serializers.SlugRelatedField(
        slug_field='title',
        queryset=Collection.objects.all(),
    )

    class Meta:
        model = Bookmark
        fields = '__all__'


class CollectionSerializer(serializers.ModelSerializer):
    bookmarks = BookmarkSerializer(read_only=True, many=True)

    class Meta:
        model = Collection
        fields = '__all__'
