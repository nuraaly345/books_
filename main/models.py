from django.db import models


class Books(models.Model):
    title=models.CharField(max_length=100)
    subtitle=models.CharField(max_length=100)
    description=models.TextField()
    price=models.CharField(max_length=100)
    genre=models.CharField(max_length=20)
    author=models.CharField(max_length=20)
    year=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)
    is_favorite=models.BooleanField(default=False)

    def __str__(self):
        return self.title
