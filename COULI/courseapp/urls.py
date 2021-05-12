
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('connexion', views.connexion, name='connexion'),
    path('chapitre/<str:slug>', views.chapitre, name='chapitre'),
    path('detailchapitre/<str:slug>', views.detailChapitre, name='detailChapitre'),
    # path("ChapitresView", views.ChapitresView.as_view(), name="ChapitresView"),
    
    ################## Admin dashboard ###########
    path('indexAdmin', views.indexAdmin, name='indexAdmin'),
    path('addAdmin', views.addAdmin, name='addAdmin'),
    path('addChap', views.addChap, name='addChap'),

]
