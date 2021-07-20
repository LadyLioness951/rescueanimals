from botocore.retries import bucket
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
import uuid
import boto3
import os
from .models import Animal, Immunization, Photo
from .forms import VisitForm

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
    immunizations_animal_doesnt_have = Immunization.objects.exclude(id__in=animal.immunizations.filter(type = animal.type).values_list('id'))
    visit_form = VisitForm()
    return render(request, 'animals/detail.html', { 
        'animal': animal,
        'visit_form': visit_form,
        'immunizations': immunizations_animal_doesnt_have
    })

class AnimalCreate(CreateView):
    model = Animal
    fields = ['name', 'type', 'breed', 'description', 'age'] 

class AnimalUpdate(UpdateView):
    model = Animal
    fields = ['type', 'breed', 'description', 'age']

class AnimalDelete(DeleteView):
    model = Animal
    success_url = '/animals/'

def add_visit(request, animal_id):
    form = VisitForm(request.POST)
    if form.is_valid():
        new_visit = form.save(commit=False)
        new_visit.animal_id = animal_id
        new_visit.save()
    return redirect('detail', animal_id=animal_id)

def add_photo(request, animal_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, animal_id=animal_id)
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', animal_id=animal_id)

class ImmunizationList(ListView):
    model = Immunization

class ImmunizationDetail(DetailView):
    model = Immunization

class ImmunizationCreate(CreateView):
    model = Immunization
    fields = '__all__'
    success_url = '/immunization/create/'

class ImmunizationUpdate(UpdateView):
    model = Immunization
    fields = '__all__'

class ImmunizationDelete(DeleteView):
    model = Immunization
    success_url = '/immunizations/'

def assoc_immunization(request, animal_id, immunization_id):
    Animal.objects.get(id=animal_id).immunizations.add(immunization_id)
    return redirect('detail', animal_id=animal_id)

