from django.db import models
from django.contrib.auth.models import User

class RezultatTest(models.Model):
    # ForeignKey permite mai multe rezultate pentru același utilizator
    utilizator = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Adăugăm default=0.0 pentru a evita eroarea de migrare
    procent_flegmatic = models.FloatField(default=0.0)
    procent_coleric = models.FloatField(default=0.0)
    procent_sangvin = models.FloatField(default=0.0)
    procent_melancolic = models.FloatField(default=0.0)
    
    data_completarii = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.utilizator.username} - {self.data_completarii.strftime('%d/%m/%Y')}"