# Test de Temperament (Scop educațional)

Aplicație web dezvoltată în Django pentru evaluarea temperamentului bazată pe cele patru tipologii clasice: **Coleric, Sangvin, Flegmatic și Melancolic**. Utilizatorii pot completa un test de 80 de întrebări și pot vizualiza rezultatele sub formă de grafice comparative.

## Funcționalități
-  **Autentificare completă**: Înregistrare utilizator, Login și Logout.
-  **Test Interactiv**: 80 de întrebări cu validare (nu se pot omite întrebări).
-  **Rezultate Vizuale**: Grafice de progres colorate pentru fiecare temperament.
-  **Istoric**: Posibilitatea de a vedea toate testele efectuate anterior.
-  **Localizare**: Interfață completă în limba română.
-  **Design Responsiv**: Stil modern, curat și ușor de utilizat de pe orice dispozitiv.

## Tehnologii folosite
- **Backend**: Python 3.13 + Django 6.0
- **Frontend**: HTML5, CSS3 (Flexbox/Grid)
- **Bază de date**: SQLite (implicit)
- **Containerizare**: Docker & Docker Compose

## Instalare și Rulare (cu Docker)

Dacă ai Docker instalat, procesul este extrem de simplu:

1. **Clonează repository-ul:**
   ```bash
   git clone [https://github.com/EmanuelUntesu/test-temperament.git]
   cd test-temperament
Pornește containerele:

Bash
docker-compose up --build
Migrează baza de date (doar la prima rulare):
Deschide un alt terminal și rulează:

Bash
docker-compose exec web python manage.py migrate
Accesează aplicația:
Deschide browserul la adresa http://localhost:8000.

Instalare Locală (fără Docker)
Creează un mediu virtual:

Bash
python -m venv venv
source venv/bin/activate  # Pe Windows: venv\Scripts\activate
Instalează dependențele:

Bash
pip install -r requirements.txt
Rulează migrarile și pornește serverul:

Bash
python manage.py migrate
python manage.py runserver

Metodologie de Calcul
Aplicația utilizează un algoritm bazat pe două tabele de referință:

Tabelul de chei: Verifică răspunsurile DA/NU pentru fiecare din cele 80 de întrebări.

Tabelul de conversie: Transformă punctajul brut în procente specifice fiecărui temperament conform standardelor psihologice de testare.

Licență
Acest proiect este creat în scop educațional.