from django.db import models


class Image(models.Model):
    file = models.ImageField(upload_to='images/')