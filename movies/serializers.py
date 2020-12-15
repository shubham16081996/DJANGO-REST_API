from rest_framework import serializers
from .models import AllMovies


class MovieSerializer(serializers.ModelSerializer):
    Poster = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = AllMovies
        fields = ['id', 'Name', 'Duration', 'Rating', 'Type', 'Year', 'Poster']
