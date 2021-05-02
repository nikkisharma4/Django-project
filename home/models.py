from django.db import models
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    phone = models.IntegerField()
    email = models.EmailField()
    dogname = models.CharField(max_length=100, default="")
    desc = models.TextField(max_length=300, default="")
    date= models.DateField()

    def __str__(self):
        return self.name
    
class Feedback(models.Model):
    text = models.CharField(max_length=100)
    textarea = models.CharField(max_length=300)
    date = models.DateField()
    
    def __str__(self):
        return self.text
    
class Gallary(models.Model):
    image   = models.ImageField(upload_to='media/', default='')
    textpara= models.CharField(null=True, max_length=300)
    date = models.DateField()
    

def get_absolute_url(self): 
    return reverse('feedback')



    