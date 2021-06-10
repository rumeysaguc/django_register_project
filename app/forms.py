from app.models.model1 import Person
from django import forms

class PersonForm(forms.ModelForm):
    
    class Meta:
        model = Person
        fields = ['name','surname','type']
