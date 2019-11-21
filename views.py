from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from django.template import loader
from django.http import Http404
from .serializers import PublicSerializer
from .serializers import PrivateSerializer
from .serializers import UserSerializer
from .serializers import SongSerializer
from .models import PublicPlaylist
from .models import PrivatePlaylist
from .models import User
from .models import Song


class PublicViewSet(viewsets.ModelViewSet):
    queryset = PublicPlaylist.objects.all().order_by('name')
    serializer_class = PublicSerializer


class PrivateViewSet(viewsets.ModelViewSet):
    queryset = PrivatePlaylist.objects.all().order_by('name')
    serializer_class = PrivateSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all().order_by('name')
    serializer_class = SongSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('last_name')
    serializer_class = UserSerializer


'''def public_id(request, p_id):
    try:
        output = PublicPlaylist.objects.get(pk=p_id)
    except PublicPlaylist.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'myapi/public_id.html', {'Playlist': output})
def public_id(playlist_id):
    output = PublicPlaylist.objects.get(id=1)
    template = loader.get_template('myapi/public_id.html')
    context = {
        'Public playlist': output,
    }
    return HttpResponse(template.render(context, output))


def private_id(playlist_id):
    output = PrivatePlaylist.objects.get(id=1)
    template = loader.get_template('myapi/private_id.html')
    context = {
        'Private playlist': output,
    }
    return HttpResponse(template.render(context, output))
'''