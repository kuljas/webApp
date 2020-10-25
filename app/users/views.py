from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from .models import *
from django.db.models import Max
from django.contrib import messages

# Create your views here.    
from .forms import CreateUserForm



def homePage(request):
    context={}
    return render(request,'users/home.html',context)


@login_required()
def korisnikPage(request, pk_test):
    korisnik = User.objects.get(id=pk_test)
    try:
        oglasivac = Oglasivac.objects.get(id=pk_test)
        oglaseni_predmeti = oglasivac.predmet_set.all()
        for predmet in oglaseni_predmeti:
            predmet.br_ponuda = predmet.bider.all().count()
            predmet.max_ponuda = predmet.bid_set.all().aggregate(Max('ponuda'))['ponuda__max']
    except Oglasivac.DoesNotExist:
        oglaseni_predmeti = None

    context={'oglaseni_predmeti':oglaseni_predmeti,'korisnik':korisnik}
    return render(request,'users/korisnik.html',context)


def predmetiPage(request):
    predmeti = Predmet.objects.all()
    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.warning(request, "Morate biti ulogovani.")

    context={'predmeti':predmeti}
    return render(request,'users/predmeti.html',context)

def about(request):

    return HttpResponse('About page')

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Profil uspesno kreiran pod imenom: '+user)
            return redirect('login')



    context={'form':form}
    return render(request,'users/register.html',context)

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            korisnik = request.user
            login(request, user)
            return redirect('/korisnik/'+str(korisnik.id))
        else:
            messages.info(request, "Username ili password su pogresni.")

    context={}
    return render(request,'users/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('home')