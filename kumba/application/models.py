from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    
    def __init__(self):
        return self.username
    
    tel = models.CharField(max_length=100)
    pays = models.CharField(max_length=100)
    profile_photo = models.URLField()

class Category(models.Model):
    
    def __init__(self):
        return self.libelle
    
    libelle = models.CharField(max_length=100)
    splot = models.CharField(max_length=100) 

class Livres(models.Model): 
    
    def __init__(self):
        return self.date_publication
    
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
    author = models.ForeignKey(User, on_delete=models.CASCADE)  

class Favoris(models.Model):
    
    def __init__(self):
        return self.name
    
    name = models.ForeignKey(User, on_delete=models.CASCADE) 
    livre = models.ForeignKey(Livres, on_delete=models.CASCADE)