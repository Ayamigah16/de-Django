from django import forms
from myapp.models import Student, Employee
from django import forms 

class StudForm(forms.Form):
    firstname = forms.CharField(label="Enter first name", max_length=20)
    lastname = forms.CharField(label="Enter last name", max_length=20)
    email = forms.EmailField(label="Enter Email")
    file = forms.FileField()  # for creating file input
    
    
    #class Meta:            ...when using student database
    #    model = Student
    #    fields = "__all__"
    
class EmpForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"