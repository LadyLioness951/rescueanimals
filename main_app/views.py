from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Animal, Immunization
from .forms import VisitForm

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
    visit_form = VisitForm()
    return render(request, 'animals/detail.html', { 
        'animal': animal,
        'visit_form': visit_form
        })

class AnimalCreate(CreateView):
    model = Animal
    fields = '__all__' 

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

class ImmunizationList(ListView):
    model = Immunization

class ImmunizationDetail(DetailView):
    model = Immunization

class ImmunizationCreate(CreateView):
    model = Immunization
    fields = '__all__'

class ImmunizationUpdate(UpdateView):
    model = Immunization
    fields = ['name', 'date']

class ImmunizationDelete(DeleteView):
    model = Immunization
    success_url = '/immunizations/'