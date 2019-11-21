from rest_framework import serializers
from .models import PublicPlaylist
from .models import PrivatePlaylist
from .models import User
from .models import Song


class PublicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PublicPlaylist
        fields = ('name', 'songs')


class PrivateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PrivatePlaylist
        fields = ('name', 'songs')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'phone')


class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = ('name', 'artist')
