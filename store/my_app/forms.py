from django import forms
from .models import Ordering


class NameForm(forms.ModelForm):
  class Meta:
    model = Ordering
    fields = '__all__'