from django.db import models
import os
from django.conf import settings

class UsersFiles(models.Model):
    title = models.CharField(max_length=20)
    file=models.FileField(upload_to='files')
    userName = models.CharField(max_length=150)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)


class UsersImage(models.Model):
    title = models.CharField(max_length=20)
    image=models.ImageField(upload_to='image')
    username = models.CharField(max_length=150)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)
