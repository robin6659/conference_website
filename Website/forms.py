from django.forms import ModelForm
from .models import Queries


# from Website import models

class ContactForm(ModelForm):
    
    class Meta:
      model = Queries
      fields = '__all__'
