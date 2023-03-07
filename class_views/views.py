from django.shortcuts import render
from django.http import HttpResponse
from django.views import View 

from .models import Tutor
from .forms import TutorForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView        # to create an instance of a table;  to update a particluar instance of the table in a database
from django.views.generic.list import ListView   # to display multiple instances of a table in a databases
from django.views.generic.detail import DetailView  # to display specific instance of a table in a database     

from django.urls import reverse_lazy, reverse
# Create your views here.

# creating a class based view
class NewView(View):
    def get(self, request):
        # TODO -- add view logic
        return HttpResponse('reponse')
    
    
# using CreateView
class TutorCreate(CreateView):
    model = Tutor
    fields = '__all__'
    success_url = reverse_lazy('class_views: TutorList')
    template_name = 'class_views/tutor_form.html'
    
# to list all instances of the table
class TutorList(ListView):
    model = Tutor
    success_url = reverse_lazy('class_views: TutorList')
    template_name = 'class_views/tutor_list.html'

# to list a specific instace of the table 
class TutorDetail(DetailView):
    model = Tutor
    success_url = reverse_lazy('class_views: TutorList')
    template_name = 'class_views/tutor_detail.html'
    
class TutorUpdate(UpdateView):
    model = Tutor
    fields = '__all__'
    template_name_suffix = "_update_form"
    success_url = reverse_lazy('class_views: TutorList')
    template_name = 'class_views/tutor_form.html'
    
class TutorDeleteView(DeleteView):
    model = Tutor
    success_url = reverse_lazy('TutorList')
    template_name = 'class_views/tutor_confirm_delete.html'