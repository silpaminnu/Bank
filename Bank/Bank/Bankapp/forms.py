
from django import forms
from .models import Person, District,Branches
class PersonCreationForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ["name","Date","Age","Phone_number","Email","Address","District","Branches","AccountType","Gender"]