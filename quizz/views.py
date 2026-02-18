from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from .questions import LISTA_INTREBARI
from .logic import calculeaza_rezultate
from .models import RezultatTest

@login_required
def pagina_test(request):
    # Traducem întrebările "din mers" pentru afișare în limba curentă a utilizatorului
    intrebari_traduse = [
        {'id': q['id'], 'text': _(q['text'])} 
        for q in LISTA_INTREBARI
    ]

    if request.method == "POST":
        raspunsuri_raw = request.POST
        raspunsuri_prelucrate = {}

        for intrebare in LISTA_INTREBARI:
            cheie = f"q{intrebare['id']}"
            valoare = raspunsuri_raw.get(cheie)
            
            # Verificăm dacă răspunsul este pozitiv. 
            # Includem și "OUI" pentru cazul în care formularul trimite textul tradus.
            raspunsuri_prelucrate[intrebare['id']] = valoare in ["DA", "OUI", "YES"]

        # Calculăm rezultatele folosind logica existentă
        procente = calculeaza_rezultate(raspunsuri_prelucrate)

        # Salvăm rezultatul în baza de date
        RezultatTest.objects.create(
            utilizator=request.user,
            procent_flegmatic=procente['flegmatic'],
            procent_coleric=procente['coleric'],
            procent_sangvin=procente['sangvin'],
            procent_melancolic=procente['melancolic']
        )
        return redirect('pagina_rezultate')

    return render(request, 'quizz/test.html', {'intrebari': intrebari_traduse})

@login_required
def pagina_rezultate(request):
    # Luăm toate rezultatele utilizatorului curent, ordonate descrescător după dată
    istoric_rezultate = RezultatTest.objects.filter(utilizator=request.user).order_by('-data_completarii')
    
    return render(request, 'quizz/rezultate.html', {'rezultate': istoric_rezultate})

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'