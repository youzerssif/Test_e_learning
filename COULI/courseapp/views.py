from django.shortcuts import render

# Create your views here.


def home(request):

    data = {}
    return render(request, 'index.html', data)



def connexion(request):

    data = {}
    return render(request, 'connexion.html', data)


def chapitre(request):
    
    data = {
        # 'slug':slug,
    }
    return render(request, 'chapitre.html', data)


def detailChapitre(request):
    
    data = {
        # 'slug':slug,
    }
    return render(request, 'detail-chapitre.html', data)


############################## Dashboard views #################

def indexAdmin(request):
    
    data = {
        # 'slug':slug,
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