from bookmarks.models import Collection, Bookmark
from rest_framework import serializers


class BookmarkSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='email',
        read_only=True)
    collections = serializers.SlugRelatedField(
        many=True,
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
        if self.context['request'].method == 'POST':
            if Bookmark.objects.filter(author=author, link=link).exists():
                raise serializers.ValidationError(
                    'This bookmark has already been added by you!'
                )
        return attrs


class CollectionSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='email',
        read_only=True)
    bookmarks = serializers.SlugRelatedField(
        many=True,
        slug_field='title',
        queryset=Bookmark.objects.all()
    )

    class Meta:
        model = Collection
        fields = '__all__'
