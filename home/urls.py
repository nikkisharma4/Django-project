from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('gallary', views.gallary, name='gallary'),
    path('feedback', views.feedback, name='feedback'),
    path('delete/<int:pk>/', views.Deletemyreview.as_view()),
    

]

