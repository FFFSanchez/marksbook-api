from django.db import models
from api.models import MyUser

import os
from django.core.files import File
from urllib.request import urlopen
from tempfile import NamedTemporaryFile
import urllib.request


class Collection(models.Model):
    title = models.CharField(max_length=200)
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
    image_file = models.ImageField(
        'Picture',
        upload_to='pictures/',
        blank=True,
        null=True,
    )
    image_url = models.URLField()
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

    def get_remote_image(self):
        if self.image_url and not self.image_file:
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(urlopen(self.image_url).read())
            img_temp.flush()
            self.image_file.save(f"image_{self.pk}", File(img_temp))

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.get_remote_image()
