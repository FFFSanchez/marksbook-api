from django.contrib import admin

from bookmarks.models import Bookmark, BookmarksCollections, Collection

from .models import MyUser


class CollectionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'description',
        'author',
        'pub_date',
        'last_update'
    )
    search_fields = ('title',)
    list_filter = ('pub_date',)
    empty_value_display = '-nothing-'


class BookmarkAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'link',
        'type_of_link',
        'image_file',
        'image_url',
        'author',
        'pub_date',
        'last_update'
    )
    search_fields = ('title',)
    list_filter = ('pub_date',)
    empty_value_display = '-nothing-'


admin.site.register(Collection, CollectionAdmin)
admin.site.register(Bookmark, BookmarkAdmin)
admin.site.register(BookmarksCollections)
admin.site.register(MyUser)
