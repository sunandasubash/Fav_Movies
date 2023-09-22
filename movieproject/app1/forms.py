from django import forms

from app1.models import Movie

class movieform(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name','des','year','img']
