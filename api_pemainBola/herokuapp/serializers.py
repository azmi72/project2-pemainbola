from django.db.models.base import Model
from django.db.models.query import QuerySet
from rest_framework import fields, serializers
from .models import PemainBola, Klub, Favorite
from django.contrib.auth.models import User


class RegistrationSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(max_length=50, min_length=6)
    username = serializers.CharField(max_length=50, min_length=6)
    password = serializers.CharField(max_length=50, write_only=True)

    class Meta:
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
            'password'
        )
        model = User

    def validate(self, args):
        email = args.get('email', None)
        username = args.get('username', None)
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': ('email already exists')})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username': ('username already exists')})

        return super().validate(args)

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)


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

class UserSerializer(serializers.ModelSerializer):
    paraPemainBola = serializers.PrimaryKeyRelatedField(many=True, queryset=PemainBola.objects.all())
    paraKlub = serializers.PrimaryKeyRelatedField(many=True, queryset=Klub.objects.all())

    class Meta:
        fields = (
            'id',
            'username',
            'email',
            'pemainbola',
            'klub'
        )
        model = User
        
class FavoriteSerializer(serializers.ModelSerializer):
    paraPemainBola = PemainBolaSerializer(read_only=True, many=True)
    paraKlub = KlubSerializer(read_only=True, many=True)

    class Meta:
        fields = (
            'favorite_id',
            'pemainbola',
            'klub'
        )
        model = Favorite