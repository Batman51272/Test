from django.contrib import admin
from Aown import views
from django.urls import path , include

urlpatterns = [
    path('' , views.index , name="home"),
    path('about' , views.about , name='about'),
    path('skills' , views.skills , name= 'skills'),
    path('contact' , views.contact , name='contact'),
    path('contact_success' , views.contact_success)
]