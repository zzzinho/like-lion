from django import forms

from .models import Jasoseol

class JssForm(forms.ModelForm):
    class Meta:
        model = Jasoseol
        # fields = '__all__'
        fields = ('title', 'body',)