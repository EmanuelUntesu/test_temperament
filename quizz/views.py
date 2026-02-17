from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .questions import LISTA_INTREBARI
from .logic import calculeaza_rezultate
from .models import RezultatTest

@login_required
def pagina_test(request):
    if request.method == "POST":
        # Colectăm răspunsurile din formular
        # Formularul trimite date de tipul {'q1': 'DA', 'q2': 'NU', ...}
        raspunsuri_raw = request.POST
        raspunsuri_prelucrate = {}

        for intrebare in LISTA_INTREBARI:
            cheie = f"q{intrebare['id']}"
            valoare = raspunsuri_raw.get(cheie)
            
            # Convertim 'DA' în True și 'NU' în False pentru logica de calcul
            raspunsuri_prelucrate[intrebare['id']] = (valoare == "DA")

        # Calculăm procentele folosind funcția din logic.py
        procente = calculeaza_rezultate(raspunsuri_prelucrate)

        # Salvăm în baza de date
        RezultatTest.objects.create(
            utilizator=request.user,
            procent_flegmatic=procente['flegmatic'],
            procent_coleric=procente['coleric'],
            procent_sangvin=procente['sangvin'],
            procent_melancolic=procente['melancolic']
        )

        return redirect('pagina_rezultate')

    # Dacă e cerere de tip GET, afișăm întrebările
    return render(request, 'quizz/test.html', {'intrebari': LISTA_INTREBARI})

@login_required
def pagina_rezultate(request):
    # Luăm toate rezultatele utilizatorului curent, ordonate după dată (cele mai noi primele)
    istoric_rezultate = RezultatTest.objects.filter(utilizator=request.user).order_by('-data_completarii')
    
    return render(request, 'quizz/rezultate.html', {'rezultate': istoric_rezultate})


from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'