from django.db import models

# Create your models here.

class Klub(models.Model):
    namaKlub = models.CharField(max_length=100)
    presiden = models.CharField(max_length=100)
    negaraKlub = models.CharField(max_length=100)
    namaLiga = models.CharField(max_length=100)
    tahunBerdiri = models.IntegerField()
    logo = models.URLField()
    data_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-data_created']

    def __str__(self):
        return self.namaKlub

class PemainBola(models.Model):
    nama = models.CharField(max_length=100)
    noPunggung = models.IntegerField()
    asalKlub = models.ForeignKey(Klub, related_name='klub', on_delete=models.CASCADE)
    asalNegara = models.CharField(max_length=100)
    umur = models.IntegerField()
    role = models.CharField(max_length=50)
    gambar = models.URLField()
    data_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-data_created']

    def __str__(self):
        return self.nama

