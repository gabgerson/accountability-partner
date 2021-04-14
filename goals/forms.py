from .models import Step
from django import forms

class StepForm(forms.ModelForm):
    class Meta:
        model = Step
        fields = ['title', 'progress', 'done']
        # labels = {'url': 'YouTube Url'}

class SearchForm(forms.Form):
    pass
#     search_term = forms.CharField(max_length=255, label='Search for Videos')