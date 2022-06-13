from asyncio.windows_events import NULL
from contextlib import nullcontext
from dataclasses import fields
from operator import contains
from pyexpat import model
from wsgiref.validate import validator
from django.forms import IntegerField
from pkg_resources import require
from rest_framework import serializers
from chinook.models import Album, Artist, Genre, Playlist, Track, Customers
#from django.contrib.auth.hashers import make_password
from django.core.validators import validate_email


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'
        depth = 1

######################################################################################

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

######################################################################################

class GenreSerializer(serializers.ModelSerializer):
    tracks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Genre
        fields = '__all__'

######################################################################################

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        #fields = '__all__'
        fields = ['id', 'name', 'composer']
      
######################################################################################


class TrackSimplifiedSerializer(serializers.ModelSerializer):

    def get_duration(self, obj):
        total_seconds = obj.milliseconds/1000

        minutes = total_seconds // 60
        seconds = total_seconds - minutes*60

        return f'{minutes}min {seconds}s'

    class Meta:
        model = Track
        #fields = ('id', 'name', 'composer', 'album_name', 'duration')
        fields = ['id', 'name', 'composer']

######################################################################################

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['name']

######################################################################################

class CustomersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customers
        fields = ['id','first_name', 'last_name', 'email', 'phone']

    def save(self):
       cadastro = Customers(  
        first_name=self.validated_data['first_name'],
        last_name=self.validated_data['last_name'],
        email=self.validated_data['email'], 
        phone=self.validated_data['phone']
    )

######################################################################################
#     

class ListCustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ['id', 'first_name', 'last_name', 'email', 'phone']



######################################################################################

def positive_only_validator(value):
    if value < 1970:
        raise serializers.ValidationError('O ano mínimo no campo é 1970!')
    elif value > 2100:
        raise serializers.ValidationError('O ano máximo no campo é 2100!')


class ObjJsonSerializer(serializers.ModelSerializer):
    year = serializers.IntegerField(validators=[positive_only_validator])
    class Meta:
        model = Customers
        fields = ['id', 'first_name', 'last_name', 'email', 'year']


########################################################################################


class ReportDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ['id','first_name', 'last_name', 'company', 'address', 'city', 'state', 'country', 'phone', 'postal_code', 'email'];

