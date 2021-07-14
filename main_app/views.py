from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Animal
from main_app import models

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')    

def animals_index(request):
    animals = Animal.objects.all()
    return render(request, 'animals/index.html', { 'animals': animals })

def animals_detail(request, animal_id):
    animal = Animal.objects.get(id=animal_id)
    return render(request, 'animals/detail.html', { 'animal': animal })

class AnimalCreate(CreateView):
    model = Animal
    fields = '__all__' 

class AnimalUpdate(UpdateView):
    model = Animal
    fields = ['type', 'breed', 'description', 'age']

class AnimalDelete(DeleteView):
    model = Animal
    success_url = '/animals/'
