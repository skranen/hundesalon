from django.db import models
class Hunderasse(models.Model):
    rasse = models.CharField(max_length=200)

    def __str__(self):
        return self.rasse

    class Meta:
        verbose_name_plural = 'Rassen'
class Kunde(models.Model):
    hundename = models.CharField(max_length=200)
    Rasse = models.ForeignKey(Hunderasse, on_delete=models.SET_NULL, blank=True, null=True)
    birth = models.DateField(blank=True, null=True)
    versichertennummer = models.BooleanField(default=False)
    besonderheiten = models.CharField(max_length=800, blank=True, null=True)

    #kunde
    name = models.CharField(max_length=200)
    vorname = models.CharField(max_length=200)
    tel = models.CharField(max_length=200, blank=True, null=True)
    adresse = models.CharField(max_length=200)
    plz = models.CharField(max_length=20)
    ort = models.CharField(max_length=300)

    def __str__(self):
        return self.hundename

    class Meta:
        verbose_name_plural = 'Kunden'

class Bilder(models.Model):
    bild = models.FileField(upload_to="")
    kunde = models.ForeignKey(Kunde, on_delete=models.CASCADE, blank=True, null=True)
    anzeigebild = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Bilder'

class Bemerkungen(models.Model):
    text = models.CharField(max_length=8000)
    kunde = models.ForeignKey(Kunde, on_delete=models.CASCADE, blank=True, null=True)
    taetigkeit = models.BooleanField(default=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = 'Bemerkungen'