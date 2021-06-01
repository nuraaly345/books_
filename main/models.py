from django.db import models


class Books(models.Model):
    title=models.CharField('Китептин аты',max_length=100)
    subtitle=models.CharField('Кыскача аныктама',max_length=100)
    description=models.TextField('Китепти сүрөттө')

    price=models.CharField('Китептин баасы',max_length=100)
    genre=models.CharField('Жанры',max_length=20)
    author=models.CharField('Автору',max_length=20)

    year=models.CharField('Чыккан жылы',max_length=100)
    date=models.DateTimeField(auto_now_add=True)
    is_favorite=models.BooleanField(default=False)

    def __str__(self):
        return self.title
