from django.forms import ModelForm
from .models import *



class OgiForm(ModelForm):
    class Meta:
        model = Ogi
        fields = ('name', 'email', 'title', 'status', 'department', 'context', 'description')


