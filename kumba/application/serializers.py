from rest_framework.serializers import ModelSerializer
from .models import *


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'        
        
class LivresSerializer(ModelSerializer):
    class Meta:
        model = Livres
        fields = '__all__'    
        
class FavorisSerializer(ModelSerializer):
    class Meta:
        model = Favoris
        fields = '__all__'           