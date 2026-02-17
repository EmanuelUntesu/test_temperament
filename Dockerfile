# Folosim o versiune ușoară de Python
FROM python:3.13-slim

# Setăm folderul de lucru în interiorul "cutiei"
WORKDIR /app

# Dezactivăm scrierea fișierelor .pyc și activăm afișarea log-urilor în timp real
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instalăm dependențele
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiem tot proiectul în "cutie"
COPY . /app/

# Portul pe care va rula Django
EXPOSE 8000

# Comanda care pornește aplicația
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]