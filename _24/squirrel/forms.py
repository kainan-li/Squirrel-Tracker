
from django.forms import ModelForm
from django.utils.translation import gettext as _
from .models import squirrel

class SquirrelForm(ModelForm):
    class Meta:
        model = squirrel
        fields ='__all__'
