from django.shortcuts import render, get_object_or_404, redirect
from .models import ExclusiveItem
from django.contrib.auth.decorators import login_required
from kho.models import UserMusic
from index.models import Music
from django.contrib import messages
from rest_framework import generics
from .serializers import ExclusiveSerializer

class ExclusiveItemUploadAPI(generics.CreateAPIView):
    queryset = ExclusiveItem.objects.all()
    serializer_class = ExclusiveSerializer

def home(request):
    items = ExclusiveItem.objects.all().order_by('-created_at')[:6]
    return render(request, 'exclusive/home.html', {'exclusive_items': items})

def all_items(request):
    items = ExclusiveItem.objects.all().order_by('-created_at')
    next_url = request.GET.get('next', '/docquyen/')
    return render(request, 'exclusive/all.html', {
        'exclusive_items': items,
        'next_url': next_url
    })

def exclusive_detail(request, pk):
    if not request.user.is_authenticated:
        messages.warning(request, "Vui lòng đăng nhập để xem nội dung độc quyền!")
        return redirect('/accounts/login/?next=' + request.path)

    item = get_object_or_404(ExclusiveItem, pk=pk)

    is_downloaded = UserMusic.objects.filter(
        user=request.user,
        source_id=item.id,
        source_type='exclusive',
        type='download'
    ).exists()

    is_favorited = UserMusic.objects.filter(
        user=request.user,
        source_id=item.id,
        source_type='exclusive',
        type='favorite'
    ).exists()

    next_url = request.GET.get('next') or request.META.get('HTTP_REFERER') or '/docquyen/'

    return render(request, 'exclusive/detail.html', {
        'item': item,
        'type': 'exclusive',
        'is_downloaded': is_downloaded,
        'is_favorited': is_favorited,
        'next_url': next_url
    })

@login_required(login_url='/accounts/login/')
def add_download(request, type, id):
    item = get_object_or_404(ExclusiveItem, id=id)

    UserMusic.objects.get_or_create(
        user=request.user,
        source_id=item.id,
        source_type='exclusive',
        type='download',
        defaults={
            'title': item.title,
            'image': item.image,
            'audio': item.audio,
        }
    )

    next_url = request.GET.get('next', '/')
    return redirect(next_url)

@login_required(login_url='/accounts/login/')
def add_favorite(request, type, id):
    item = get_object_or_404(ExclusiveItem, id=id)

    UserMusic.objects.get_or_create(
        user=request.user,
        source_id=item.id,
        source_type='exclusive',
        type='favorite',
        defaults={
            'title': item.title,
            'image': item.image,
            'audio': item.audio,
        }
    )

    next_url = request.GET.get('next', '/')
    return redirect(next_url)

@login_required(login_url='/accounts/login/')
def remove_download(request, type, id):
    UserMusic.objects.filter(
        user=request.user,
        source_id=id,
        source_type='exclusive',
        type='download'
    ).delete()
    next_url = request.GET.get('next', '/')
    return redirect(next_url)

@login_required(login_url='/accounts/login/')
def remove_favorite(request, type, id):
    UserMusic.objects.filter(
        user=request.user,
        source_id=id,
        source_type='exclusive',
        type='favorite'
    ).delete()
    next_url = request.GET.get('next', '/')
    return redirect(next_url)

@login_required(login_url='/accounts/login/')
def user_library(request):
    user_items = UserMusic.objects.filter(user=request.user)

    downloads = []
    favorites = []

    for u in user_items:
        try:
            if u.source_type == 'exclusive':
                item = ExclusiveItem.objects.get(id=u.source_id)
            elif u.source_type == 'music':
                item = Music.objects.get(id=u.source_id)
            else:
                continue
        except (ExclusiveItem.DoesNotExist, Music.DoesNotExist):
            continue

        if u.type == 'download':
            downloads.append(item)
        elif u.type == 'favorite':
            favorites.append(item)

    return render(request, 'kho/library.html', {
        'downloads': downloads,
        'favorites': favorites
    })