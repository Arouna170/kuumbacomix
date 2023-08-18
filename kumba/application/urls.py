from django.urls import path, include
from rest_framework import routers
 
from .views import *
 

router = routers.SimpleRouter()

router.register('user', UserViewset, basename='user')
router.register('categorie', CategoryViewset, basename='categorie')
router.register('livres', LivresViewset, basename='livres')
router.register('favoris', FavorisViewset, basename='favoris')

urlpatterns = [
    path('api/', include(router.urls)),
]