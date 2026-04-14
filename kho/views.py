from django.shortcuts import render, get_object_or_404
from .models import UserMusic
from django.shortcuts import redirect
from rest_framework import generics
from .serializers import UserMusicSerializer

class UserMusicUploadAPI(generics.CreateAPIView):
    queryset = UserMusic.objects.all()
    serializer_class = UserMusicSerializer
    
def kho_list(request):
    downloads = UserMusic.objects.filter(type='download')[:6]
    favorites = UserMusic.objects.filter(type='favorite')[:6]

    return render(request, 'kho/kho.html', {
        'downloads': downloads,
        'favorites': favorites
    })


def kho_download_all(request):
    musics = UserMusic.objects.filter(type='download')
    return render(request, 'kho/kho_all.html', {'musics': musics})

def kho_favorite_all(request):
    musics = UserMusic.objects.filter(type='favorite')
    return render(request, 'kho/kho_all.html', {'musics': musics})

def kho_detail(request, id):
    item = UserMusic.objects.get(id=id)
    return render(request, 'kho/kho_detail.html', {'item': item})

def remove_download(request, type, id):
    if request.user.is_authenticated:
        UserMusic.objects.filter(
            user=request.user,
            source_type=type,
            source_id=id,
            type='download'
        ).delete()

    return redirect(request.GET.get('next', '/kho/'))


def remove_favorite(request, type, id):
    if request.user.is_authenticated:
        UserMusic.objects.filter(
            user=request.user,
            source_type=type,
            source_id=id,
            type='favorite'
        ).delete()

    return redirect(request.GET.get('next', '/kho/'))