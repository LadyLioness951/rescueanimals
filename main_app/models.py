from django.db import models
from django.urls import reverse

SPECIES = (
    ('C', 'Cat'),
    ('D', 'Dog'),
    ('O', 'Other'),
    ('R', 'Rabbit')
)

# Create your models here.
class Immunization(models.Model):
    name = models.CharField(max_length=150)
    type = models.CharField(
        max_length=1,
        choices=SPECIES,
        default=SPECIES[1][0]
    )

class Animal(models.Model):
    name = models.CharField(max_length=25)
    type = models.CharField(
        max_length=1,
        choices=SPECIES,
        default=SPECIES[1][0]
    )
    breed = models.CharField(max_length=50)
    description = models.TextField()
    age = models.IntegerField()
    immunizations = models.ManyToManyField(Immunization)

    def __str__(self):
        return f'{self.name} is {self.age} years old'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'animal_id': self.id})

    class Meta:
        ordering = ['type']

class Visit(models.Model):
    name = models.CharField(max_length=100)        
    phoneNumber = models.CharField(max_length=15)
    date = models.DateField('Meet & Greet Date')
    time = models.CharField(max_length=10)

    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} is coming for a meet and greet on {self.date} at {self.time}'

    class Meta:
        ordering = ['-date']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)

    def __str__(self):
        return f'Photo for animal_id: {self.animal_id} @ {self.url}'