from django.contrib.auth import login, logout
from django.db import models
from django.shortcuts import redirect

from news.forms import *


class ArticleCategory(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Kategoriya nomi")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'


class Article(models.Model):
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    photo = models.ImageField(null=True, blank=True, upload_to='photos/')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqti")
    publish_at = models.DateTimeField(auto_created=True, verbose_name="Yaratilgan vaqti")
    category = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE)
    publish = models.BooleanField(default=True)

    def get_photo(self):
        try:
            return self.photo.url
        except:
            return 'https://www.nicepng.com/png/detail/0-7565_no-photography-sign-png-no-photography-allowed-signs.png'

    class Meta:
        verbose_name = "Maqola"
        verbose_name_plural = "Maqolalar"

    def __str__(self):
        return self.title



