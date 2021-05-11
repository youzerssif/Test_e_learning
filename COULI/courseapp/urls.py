
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('connexion', views.connexion, name='connexion'),
    path('chapitre', views.chapitre, name='chapitre'),
    path('detailchapitre', views.detailChapitre, name='detailChapitre'),
    
    ################## Admin dashboard ###########
    path('indexAdmin', views.indexAdmin, name='indexAdmin'),
    path('addAdmin', views.addAdmin, name='addAdmin'),
    path('addChap', views.addChap, name='addChap'),

]
