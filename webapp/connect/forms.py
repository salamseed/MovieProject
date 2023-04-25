from django import forms
from .models import films
class film_form(forms.ModelForm):
    class Meta:
        model=films
        fields=['name','year','desc','image']