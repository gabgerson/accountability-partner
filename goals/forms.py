from .models import Step
from django import forms

class StepForm(forms.ModelForm):
    class Meta:
        model = Step
        fields = ['title', 'progress', 'done','deadline']
        # labels = {'url': 'YouTube Url'}

class SearchForm(forms.Form):
    pass
