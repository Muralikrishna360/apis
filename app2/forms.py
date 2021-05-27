from django.forms import ModelForm
from .models import *


class SendForm(ModelForm):
    class Meta:
        model = Send
        fields = ('fbuser', 'feedback')