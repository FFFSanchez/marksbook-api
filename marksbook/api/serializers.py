from bookmarks.models import Collection, Bookmark
from rest_framework import serializers


class BookmarkSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='email',
        read_only=True)
    collection = serializers.SlugRelatedField(
        slug_field='title',
        queryset=Collection.objects.all(),
        required=False,
    )

    class Meta:
        model = Bookmark
        fields = '__all__'
        read_only_fields = ('title', 'description', 'image_url')

    def validate(self, attrs):
        author = self.context['request'].user
        link = attrs['link']
        if Bookmark.objects.filter(author=author, link=link).exists():
            raise serializers.ValidationError(
                'This bookmark has already been added by you!'
            )
        return attrs


class CollectionSerializer(serializers.ModelSerializer):
    bookmarks = BookmarkSerializer(read_only=True, many=True)

    class Meta:
        model = Collection
        fields = '__all__'
