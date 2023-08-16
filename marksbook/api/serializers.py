from rest_framework import serializers

from bookmarks.models import Bookmark, Collection

from .tools.og_parse import get_og_info


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
            if not get_og_info(link):
                raise serializers.ValidationError(
                    'Bad link or site cant be reached!'
                )
        return attrs


class CollectionSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='email',
        read_only=True)
    
    # Maybe use slug-fields for this, to make it unique and undestandable
    bookmarks = serializers.SlugRelatedField(
        many=True,
        slug_field='id',
        queryset=Bookmark.objects.all(),
        required=False
    )

    class Meta:
        model = Collection
        fields = '__all__'
