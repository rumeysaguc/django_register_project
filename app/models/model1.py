from django.db import models
from django.db.models.base import Model

TYPE_CHOICES = (
    ('Öğretmen','öğretmen'),
    ('Müdür','müdür'),
    ('Öğrenci','öğrenci'),
)

class Person(models.Model):
    name = models.CharField(max_length=20, verbose_name='adı')
    surname = models.CharField(max_length=20, verbose_name='soyadı')
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='Müdür')
    