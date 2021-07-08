from django.db.models.base import Model
from rest_framework import fields, serializers
from .models import PemainBola, Klub


class PemainBolaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'nama',
            'noPunggung',
            'asalKlub',
            'asalNegara',
            'umur',
            'role',
            'gambar',
            'data_created'
        )
        model = PemainBola


class KlubSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'namaKlub',
            'presiden',
            'negaraKlub',
            'namaLiga',
            'tahunBerdiri',
            'logo',
            'data_created'
        )
        model = Klub