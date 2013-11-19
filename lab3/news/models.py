from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(verbose_name=u'Title', max_length=255)
    datetime = models.DateTimeField(verbose_name='Date of editing')
    comment = models.TextField(verbose_name='Comment')
