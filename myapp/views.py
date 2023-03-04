from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
import datetime
from django.template import loader
from django.views.decorators.http import require_http_methods
from myapp.form import StudForm, EmpForm
from myapp.functions.functions import handle_uploaded_file
from django.contrib.sessions.models import Session
import csv
from myapp.models import Employee
from reportlab.pdfgen import canvas
from mysite import settings
from django.core.mail import send_mail
# Create your views here.
# creating my views

# function to send a mail
def mail(request):
    subject = "Greetings"
    msg = "Abraham sent sent you a mail. Learning Django is fun."
    to = "abkc070@gmail.com"
    res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
    if(res == 1):
        msg = "Mail Sent Successfully"
    else:
        msg = "Mail could not sent"
    return HttpResponse(msg)

def getpdf(request):
    response = HttpResponse(content_type='application/pdf')  # MIME(content)
    response['Content-Disposition'] = 'attatchment;filename="myapp.pdf"'  # setting filename
    
    p = canvas.Canvas(response)
    p.setFont("Times-Roman", 55)
    p.drawString(100,700,"Hello, Abraham.")
    p.showPage()
    p.save()
    
    return response
    




@require_http_methods(["GET","POST"])
def hello(request):
    return HttpResponse("<h2>Hello, Welcom to MySite!</h2>")

 

def show(request):
    return HttpResponse('<h1>This is Http GET request</h1>')


# form validation
def stud(request):
    # checking wether the request is post or not
    if request.method == "POST":
        form = StudForm(request.POST)
        # form inputs is valid
        if form.is_valid():
            try:
                return redirect('/')
            except:
                pass
            
        else:
            form = StudForm()
        return render(request, 'index.html', {'form':form })
    
    
def emp(request):
    if request.method == 'POST':
        form = EmpForm(request.POST)
        
        if form.is_valid():
            try:
                return('/')
            except:
                pass
        else:
            form = EmpForm()
        return render(request,'index2.html',{'form':form} )
    
    
    
def index(request):
    if request.method == "POST":
        student = StudForm(request.POST, request.FILES)
        
        if student.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("File uploaded successfully")
    else:
        student = StudForm()
        return render(request, "index.html", {'form': student})
    

def index(request):
    if request.method == "POST":
        student = StudForm(request.POST, request.FILES)
        
        if student.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("File uploaded successfully")
    else:
        student = StudForm()
        return render(request, "index.html", {'form': student})
    
    
        #when using the student database in models.py
    #stu = StudForm()
    #return render(request, 'index.html', {'form':stu })
    
# sessions
def setsession(request):
    request.session['sname'] = 'Abraham'
    request.session['semail'] = 'abkc@gmail.com'
    return HttpResponse('session is set')

def getsession(request):
    studentname = request.session['sname']
    studentemail = request.session['semail']
    return HttpResponse(studentname + " " + studentemail)
    
    
# cookies
def setcookie(request):
    response = HttpResponse("Cookies set")
    response.set_cookie('django-tutorial', "Django Cookies")
    return response

def getcookie(request):
    tutorial = request.COOKIES['django-tutorial']
    return HttpResponse('django tutorials @:' + tutorial)


# csv getfile
def getfile(request):
    response = HttpResponse(content_type= 'text/csv')
    response['Content-Disposition'] = 'attatchment; filename="file.csv"'
    
    # a dynamic csv using database
    employees = Employee.objects.all()
    writer = csv.writer(response)
    for employee in employees:
        writer.writerow([employee.emp_id, employee.emp_name,employee.emp_contact])
    return response
    
    #for static csv
    #writer = csv.writer(response)
    #writer.writerow(['1001','Joel','Andoh','MA'])
    #writer.writerow(['1002', 'Jonathan','Ohene', 'EL'])
    #return response


