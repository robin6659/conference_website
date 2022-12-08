from django.forms import ModelForm
from .models import Queries


# from Website import models

class ContactForm(ModelForm):
    
    class Meta:
      model = Queries
      fields = '__all__'
 
    # this function will be used for the validation
    # def clean(self):
 
    #     # data from the form is fetched using super function
    #     super(ContFm, self).clean()
         
    #     # extract the username and text field from the data
    #     name = self.cleaned_data.get('name') 
    #     # conditions to be met for the username length
    #     # if len(name) < 20:
    #     #     self._errors['name'] = self.error_class([
    #     #         'Maximum 20 characters required'])
    #     # if len(contact_number) <10:
    #     #     self._errors['text'] = self.error_class([
    #     #         'Post Should Contain a minimum of 10 characters'])
 
    #     # return any errors if found
    #     return self.cleaned_data
        