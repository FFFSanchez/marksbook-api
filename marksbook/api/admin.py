from django.contrib import admin

from bookmarks.models import Collection, Bookmark
from .models import MyUser


class CollectionAdmin(admin.ModelAdmin):
    search_fields = ('title',)


class BookmarkAdmin(admin.ModelAdmin):
    search_fields = ('title',)


admin.site.register(Collection, CollectionAdmin)
admin.site.register(Bookmark, BookmarkAdmin)
admin.site.register(MyUser)
