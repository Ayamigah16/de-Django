from django.forms import fields
from class_views.models import Tutor
from django import forms 

class TutorForm(forms.ModelForm):
    
    class Meta:
        model = Tutor       # specifying the model to use
        fields = "__all__"      # applying all fields
        
        