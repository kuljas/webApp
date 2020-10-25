from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Oglasivac(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.user.username)

class Bider(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.user.username)

class Predmet(models.Model):
    oglasivac = models.ForeignKey(Oglasivac,null=True, on_delete=models.CASCADE)
    bider = models.ManyToManyField(Bider,blank=True)
    KATEGORIJA = (
                ('Knjige' , 'Knjige'),
                ('Oprema' , 'Oprema'),
                ('Ostalo', 'Ostalo'),
            )
    ime = models.CharField(max_length=200,null = True,blank=False)
    pocetna_cena = models.FloatField(null=True,blank=False)
    kategorija = models.CharField(max_length=200,null = True,choices=KATEGORIJA)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    trajanje_aukcije = models.DateTimeField(null=True)
    opis = models.CharField(max_length=200,null = True,blank=True)

    def __str__(self):
        return "Predmet: "+ self.ime 


class Bid(models.Model):
    bider = models.ForeignKey(Bider,null=True,on_delete=models.CASCADE)
    predmet = models.ForeignKey(Predmet,null=True,on_delete=models.CASCADE)
    ponuda = models.FloatField(null=True)

    def __str__(self):
        return "Bider: "+str(self.bider.user.username)+" - Predmet: "+str(self.predmet.ime)+" - Ponuda: "+str(self.ponuda)