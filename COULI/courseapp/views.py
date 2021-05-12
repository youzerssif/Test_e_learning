from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.db.models import Q
import json

from . import models
# from django.http import HttpResponse
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404

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


# def detailChapitre(request, slug):
    
#     chapitre = models.Chapitre.objects.get(slug=slug)
#     print(chapitre)
    
#     data = {
#         'slug':slug,
#         'chapitre':chapitre,
#     }
#     return render(request, 'detail-chapitre.html', data)

class detailchapitreView(DetailView):
    model = models.Chapitre
    template_name = 'detail-chapitre.html'

    def detailchapitre_View(request, slug):

        chapitre = get_object_or_404(models.Chapitre, slug=slug)

        return render(request, 'detail-chapitre.html', context={'chapitre': chapitre})


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


@csrf_exempt
def addCoursApi(request):
    if request.method == "POST":
        try:
            try:
                postdata = json.loads(request.body.decode('utf-8'))
                file = postdata['file']
                titre = postdata['titre']
                description = postdata['description']
            except:
                file = request.FILES.get("file")
                titre = request.POST.get("titre")
                description = request.POST.get("description")
                
          
          
            user = models.Formateur.objects.get(user=request.user)
            cours = models.Cours(formateur=user,titre=titre, description=description, image=file)
            cours.save()
            
            url=f"addChap/{cours.slug}"
            print(url)
            success = True
            message = "Votre cours a été enregistré avec succès"
        except Exception as e:
            print(str(e))
            success = False
            message = "Une erreur est survenue veillez à contacter le Webmaster."
    else:
        success = False
        message = "Erreur de Requête"
        url=""

    data = {
        'success': success,
        'message': message,
        'url': url,
    }
    return JsonResponse(data, safe=False)


def addChap(request, slug):
    
    data = {
        'slug':slug,
    }
    return render(request, 'add-chapitre.html', data)


@csrf_exempt
def addChapApi(request):
    url=""
    if request.method == "POST":
        try:
            try:
                postdata = json.loads(request.body.decode('utf-8'))
                titre = postdata['titre']
                slug = postdata['slug']
                description = postdata['description']
            except:
                titre = request.POST.get("titre")
                description = request.POST.get("description")
                slug = request.POST.get("slug")
                
          
          
            cours = models.Cours.objects.get(slug=slug)
            print("le cours :", cours)
            chapitre = models.Chapitre(cours=cours,titre=titre, description=description,)
            chapitre.save()
            
            url="indexAdmin"
            # print(url)
            success = True
            message = "Votre chapitre a été enregistré avec succès"
        except Exception as e:
            print(str(e))
            success = False
            message = "Une erreur est survenue veillez à contacter le Webmaster."
    else:
        success = False
        message = "Erreur de Requête"
        url=""

    data = {
        'success': success,
        'message': message,
        'url': url,
    }
    return JsonResponse(data, safe=False)