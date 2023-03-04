"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from class_views.views import NewView, TutorCreate  # importing the class based view 

urlpatterns = [
    path('admin/', admin.site.urls),
    # paths for myapp
    path("hello/", views.hello),
    path('index/', views.index),
    path('show/', views.show),
    path('ssession', views.setsession),
    path('gsession', views.getsession),
    path('scookie', views.setcookie),
    path('gcookie', views.getcookie),   
    path('csv', views.getfile), #adding csv url
    path('pdf', views.getpdf),    # adding pdf url
    path('mail', views.mail),
    
    # path for classviews app
    path('about/', NewView.as_view()),   # as_view() method is used
    path("tutor/", TutorCreate.as_view(), name = 'TutorCreate')
]
