from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    tel = models.CharField(max_length=100)
    pays = models.CharField(max_length=100)
    profile_photo = models.URLField()

class Category(models.Model):
    libelle = models.CharField(max_length=100)
    splot = models.CharField(max_length=100) 

class Livres(models.Model): 
    date_publication = models.DateField()
    genre = models.CharField(max_length=200)
    nbr_page = models.IntegerField()
    is_valide = models.BooleanField()
    is_visible = models.BooleanField()
    img_link = models.URLField()  
    resume = models.TextField()
    langage = models.CharField(max_length=30)
    created_at = models.DateField(auto_now=True)
    update_at = models.DateField(auto_now=True)
    categorie = models.ForeignKey(Category, on_delete=models.CASCADE)  
    autorId = models.ForeignKey(User, on_delete=models.CASCADE)  
