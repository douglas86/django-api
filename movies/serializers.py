from rest_framework import serializers
from .models import MovieData

class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        movie = MovieData
        feilds = ['id', 'name', 'duration', 'rating']
