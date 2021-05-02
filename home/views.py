from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact, Feedback, Gallary
from django.views.generic import DeleteView, CreateView
from django.urls import reverse_lazy


# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name= request.POST.get("name")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        dogname=request.POST.get("dogname")
        desc=request.POST.get("desc")
        contact = Contact(name=name, email=email, phone=phone, dogname=dogname, desc=desc, date= datetime.today())
        contact.save()
    return render(request, 'contact.html')

def gallary(request):
    if request.method=="POST":
        image= request.POST.get('image')
        textpara=request.POST.get('textpara')
        gallary = Gallary(image=image, textpara=textpara, date=datetime.today())
        gallary.save()
        
    gal= Gallary.objects.all()
    return render(request, 'gallary.html', {'gall':gal})


    
# feedback views file 
def feedback(request):
    if request.method == "POST":
        text=request.POST.get("text")
        textarea=request.POST.get("textarea")
        feedback = Feedback(text=text, textarea=textarea, date=datetime.today())
        feedback.save() 
        
    feed = Feedback.objects.all()
    return render(request, 'feedback.html', {'feedb': feed})


class Deletemyreview(DeleteView):
    model = Feedback
    success_url= reverse_lazy('feedback')
    


# "python manage.py makemigration appname" use this command after creating new database 
# "python manage.py migrate" use this command 