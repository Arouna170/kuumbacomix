from django.contrib import admin

from .models import *

class UserAdmin(admin.ModelAdmin):  
    list_display = ('tel', 'pays', 'profile_photo') 
class CategoryAdmin(admin.ModelAdmin):  
    list_display = ('libelle', 'splot')

class LivresAdmin(admin.ModelAdmin):  
    list_display = ('date_publication', 'genre', 'resume')    

class FavorisAdmin(admin.ModelAdmin):  
    list_display = ('name', 'livre')
    
            
admin.site.register(User, UserAdmin) 
admin.site.register(Favoris, FavorisAdmin) 
admin.site.register(Livres, LivresAdmin) 
admin.site.register(Category, CategoryAdmin) 