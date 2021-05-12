from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.db.models import Q

from . import models
from django.http import HttpResponse
from django.views.generic import ListView

# Create your views here.


def home(request):

    cours = models.Cours.objects.filter(status=True)

    data = {
        "cours":cours,
    }
    return render(request, 'index.html', data)



def connexion(request):

    data = {}
    return render(request, 'connexion.html', data)

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        message, success, url = '', False, ''
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(Q(email=email) | Q(username=email) & Q(is_active=True)).first()

        if user:
            utilisateur = authenticate(username=user.username, password=password)
            if utilisateur:
                login(request, utilisateur)
                message, success = 'Connexion effectué', True
                url = "indexAdmin"
            else:
                message = 'Vos identifiants ne sont pas correctes.'
        else:
            message = "Vos identifiants n\'existent pas."
        datas = {
            'message': message,
            'success': success,
            'url': url,
        }
        return JsonResponse(datas, safe=False)


def logout_view(request):
    logout(request)
    return redirect('home')


def chapitre(request, slug):
    
    chapitres = models.Chapitre.objects.filter(status=True, cours__slug=slug)
    
    data = {
        'slug':slug,
        'chapitres':chapitres,
    }
    return render(request, 'chapitre.html', data)


def detailChapitre(request, slug):
    
    chapitre = models.Chapitre.objects.get(slug=slug)
    print(chapitre)
    
    data = {
        'slug':slug,
        'chapitre':chapitre,
    }
    return render(request, 'detail-chapitre.html', data)

# class ChapitresView(ListView):
#     model = models.Chapitre

#     def detailChapitre(self, *args, **kwargs):
#         chapitre = self.get_queryset()
#         response = HttpResponse(

#             headers={'chapitre': chapitre},
#         )
#         return response


############################## Dashboard views #################

def indexAdmin(request):
    
    mesCours = models.Cours.objects.filter(formateur__user=request.user, status=True)
    
    data = {
        'mesCours':mesCours,
    }
    return render(request, 'index-admin.html', data)


def addAdmin(request):
    
    data = {
        # 'slug':slug,
    }
    return render(request, 'add-cours.html', data)

def addChap(request):
    
    data = {
        # 'slug':slug,
    }
    return render(request, 'add-chapitre.html', data)