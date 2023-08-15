from django.db import models
from users.models import MyUser


class Collection(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    pub_date = models.DateTimeField(
        'Pub date', auto_now_add=True
    )
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Bookmark(models.Model):
    website = 'website'
    book = 'book'
    article = 'article'
    music = 'music'
    video = 'video'

    TYPE_CHOICES = (
        (website, 'website'),
        (book, 'book'),
        (article, 'article'),
        (music, 'music'),
        (video, 'video')
    )
    title = models.TextField(max_length=200)
    description = models.TextField()
    link = models.URLField()
    type_of_link = models.CharField(
        choices=TYPE_CHOICES,
        default=website,
        verbose_name='type'
    )
    image = models.ImageField(
        'Picture',
        upload_to='pictures/',
        blank=True,
        null=True,
    )
    author = models.ForeignKey(
        MyUser, on_delete=models.CASCADE, related_name='bookmarks'
    )
    pub_date = models.DateTimeField(
        'Pub date', auto_now_add=True
    )
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(
        Collection, on_delete=models.SET_NULL,
        related_name='bookmarks', blank=True, null=True
    )

    class Meta:
        verbose_name = ('Bookmark')
        verbose_name_plural = ('Bookmarks')

    def __str__(self):
        return self.title
