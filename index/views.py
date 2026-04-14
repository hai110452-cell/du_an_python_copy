from django.shortcuts import render, get_object_or_404, redirect
from .models import Music, MusicHot
from kho.models import UserMusic
from exclusive.models import ExclusiveItem
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from .serializers import MusicSerializer

class MusicUploadAPI(generics.CreateAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

class MusicHotUploadAPI(generics.CreateAPIView):
    queryset = MusicHot.objects.all()
    serializer_class = MusicSerializer

def get_user_status(request, item_id, source_type):
    if request.user.is_authenticated:
        is_downloaded = UserMusic.objects.filter(
            user=request.user,
            source_id=item_id,
            source_type=source_type,
            type='download'
        ).exists()

        is_favorited = UserMusic.objects.filter(
            user=request.user,
            source_id=item_id,
            source_type=source_type,
            type='favorite'
        ).exists()

        return is_downloaded, is_favorited

    return False, False

def index(request):
    musics = Music.objects.all().order_by('-date')[:6]
    musics_hot = MusicHot.objects.all().order_by('-date')[:6]
    exclusive_items = ExclusiveItem.objects.all().order_by('-created_at')[:6]
    return render(request, 'index/index.html', {
        'musics': musics,
        'musics_hot': musics_hot,
        'exclusive_items': exclusive_items,
    })

def music_detail(request, id):
    item = get_object_or_404(Music, id=id)
    next_url = request.GET.get('next', '/')
    is_downloaded, is_favorited = get_user_status(request, item.id, 'music')

    return render(request, 'index/detail.html', {
        'item': item,
        'type': 'music',
        'next_url': next_url,
        'is_downloaded': is_downloaded,
        'is_favorited': is_favorited
    })

def musichot_detail(request, id):
    item = get_object_or_404(MusicHot, id=id)
    next_url = request.GET.get('next', '/')
    is_downloaded, is_favorited = get_user_status(request, item.id, 'music_hot')

    return render(request, 'index/detail.html', {
        'item': item,
        'type': 'music_hot',
        'next_url': next_url,
        'is_downloaded': is_downloaded,
        'is_favorited': is_favorited
    })

def music_all(request):
    musics = Music.objects.all().order_by('-date')
    return render(request, 'index/music_all.html', {'musics': musics})

def hot_all(request):
    musics_hot = MusicHot.objects.all().order_by('-date')
    return render(request, 'index/hot_all.html', {
        'musics_hot': musics_hot
    })
@login_required(login_url='/accounts/login/')
def add_download(request, type, id):
    model_map = {'music': Music, 'music_hot': MusicHot}
    model = model_map.get(type)
    if not model:
        return redirect('/')

    item = get_object_or_404(model, id=id)

    UserMusic.objects.get_or_create(
        user=request.user,
        source_id=item.id,
        source_type=type,
        type='download',
        defaults={
            'title': item.title,
            'image': item.image,
            'audio': item.audio
        }
    )

    return redirect(request.GET.get('next') or '/kho/')

@login_required(login_url='/accounts/login/')
def add_favorite(request, type, id):
    model_map = {'music': Music, 'music_hot': MusicHot}
    model = model_map.get(type)
    if not model:
        return redirect('/')
    
    item = get_object_or_404(model, id=id)

    UserMusic.objects.get_or_create(
        user=request.user,
        source_id=item.id,
        source_type=type,
        type='favorite',
        defaults={
            'title': item.title,
            'image': item.image,
            'audio': item.audio
        }
    )

    return redirect(request.GET.get('next') or '/kho/')

@login_required(login_url='/accounts/login/')
def remove_download(request, type, id):
    UserMusic.objects.filter(
        user=request.user,
        source_id=id,
        source_type=type,
        type='download'
    ).delete()
    return redirect(request.GET.get('next') or '/')

@login_required(login_url='/accounts/login/')
def remove_favorite(request, type, id):
    UserMusic.objects.filter(
        user=request.user,
        source_id=id,
        source_type=type,
        type='favorite'
    ).delete()
    return redirect(request.GET.get('next') or '/')