from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle 
from rest_framework.authentication import TokenAuthentication
from .models import *
from .serializers import *


class UserViewset(ModelViewSet):
    
    authentication_classes = [TokenAuthentication]
    throttle_classes = [UserRateThrottle]
    serializer_class = UserSerializer
    
    def get_queryset(self):
        return User.objects.all()

class CategoryViewset(ModelViewSet):
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]
    serializer_class = CategorySerializer
    
    def get_queryset(self):
        return Category.objects.all()
    
class LivresViewset(ModelViewSet):
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]
    serializer_class = LivresSerializer
    
    def get_queryset(self):
        return Livres.objects.all()
    
class FavorisViewset(ModelViewSet):
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]
    serializer_class = FavorisSerializer
    
    def get_queryset(self):
        return Favoris.objects.all()        