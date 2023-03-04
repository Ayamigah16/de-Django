from django.shortcuts import render
from django.http import HttpResponse
from django.views import View 

from .models import Tutor
from .forms import TutorForm
from django.views.generic.edit import CreateView

# Create your views here.

# creating a class based view
class NewView(View):
    def get(self, request):
        # TODO -- add view logic
        return HttpResponse('reponse')
    
    
## using CreateView
class TutorCreate(CreateView):
    model = Tutor
    fields = '__all__'
    template_name = 'class_views/tutor_form.html'