from django import forms
from .models import AddWaitTime

class AddTimeForm(forms.ModelForm):

    class Meta:
        model = AddWaitTime
        fields = ('endereco', 'data', 'tempo')