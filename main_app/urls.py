from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('animals/', views.animals_index, name='index'),
    path('animals/<int:animal_id>/', views.animals_detail, name='detail'),
    path('animals/create/', views.AnimalCreate.as_view(), name='animals_create'),
    path('animals/<int:pk>/update/', views.AnimalUpdate.as_view(), name='animals_update'),
    path('animals/<int:pk>/delete/', views.AnimalDelete.as_view(), name='animals_delete'),
    path('animals/<int:animal_id>/add_visit/', views.add_visit, name='add_visit'),
    path('immunization/', views.ImmunizationList.as_view(), name='immunizations_index'),
    path('immunization/<int:pk>/', views.ImmunizationDetail.as_view(), name='immunizations_detail'),
    path('immunization/create/', views.ImmunizationCreate.as_view(), name='immunizations_create'),
    path('immunization/<int:pk>/update/', views.ImmunizationUpdate.as_view(), name='immunizations_update'),
    path('immunization/<int:pk>/delete/', views.ImmunizationDelete.as_view(), name='immunizations_delete'),
]