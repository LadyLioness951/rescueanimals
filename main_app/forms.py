from django.forms import ModelForm
from .models import Visit

class VisitForm(ModelForm):
    class Meta:
        model = Visit
        fields = ['name', 'phoneNumber', 'date', 'time']
        