from django.db import models
from django.urls import reverse

# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=25)
    type = models.CharField(max_length=25)
    breed = models.CharField(max_length=50)
    description = models.TextField()
    age = models.IntegerField()

    def __str__(self):
        return f'{self.name} is {self.age} years old'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'animal_id': self.id})
