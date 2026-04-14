from django.shortcuts import redirect, render, get_object_or_404
from .models import Ballad, Category, Rock, Edm,  Viet, Hiprap
from kho.models import UserMusic
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from .serializers import BalladSerializer, CategorySerializer, RockSerializer, EdmSerializer, VietSerializer, HiprapSerializer

class CategoryUploadAPI(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BalladUploadAPI(generics.CreateAPIView):
    queryset = Ballad.objects.all()
    serializer_class = BalladSerializer

class RockUploadAPI(generics.CreateAPIView):
    queryset = Rock.objects.all()
    serializer_class = RockSerializer

class EdmUploadAPI(generics.CreateAPIView):
    queryset = Edm.objects.all()
    serializer_class = EdmSerializer

class VietUploadAPI(generics.CreateAPIView):
    queryset = Viet.objects.all()
    serializer_class = VietSerializer

class HiprapUploadAPI(generics.CreateAPIView):
    queryset = Hiprap.objects.all()
    serializer_class = HiprapSerializer

@login_required(login_url='/accounts/login/')
def add_download(request, type, id):
    model_map = {
        'category': Category,
        'rock': Rock,
        'hiprap': Hiprap,
        'edm': Edm,
        'ballad': Ballad,
        'viet': Viet,

    }

    model = model_map.get(type)
    if not model:
        return redirect('/category/')

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

    return redirect(request.GET.get('next', '/category/'))

@login_required(login_url='/accounts/login/')
def add_favorite(request, type, id):
    model_map = {
        'category': Category,
        'rock': Rock,
        'hiprap': Hiprap,
        'edm': Edm,
        'ballad': Ballad,

        'viet': Viet,

    }

    model = model_map.get(type)
    if not model:
        return redirect('/category/')

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

    return redirect(request.GET.get('next', '/category/'))

@login_required(login_url='/accounts/login/')
def remove_download(request, type, id):
    UserMusic.objects.filter(
        user=request.user,
        source_id=id,
        source_type=type,
        type='download'
    ).delete()
    return redirect(request.GET.get('next', '/'))

@login_required(login_url='/accounts/login/')
def remove_favorite(request, type, id):
    UserMusic.objects.filter(
        user=request.user,
        source_id=id,
        source_type=type,
        type='favorite'
    ).delete()
    return redirect(request.GET.get('next', '/kho/'))

def category_list(request):
    categories = Category.objects.all().order_by('-date')[:6]
    rocks = Rock.objects.all().order_by('-date')[:6]
    edms = Edm.objects.all().order_by('-date')[:6]
    ballads = Ballad.objects.all().order_by('-date')[:6]
    hipraps = Hiprap.objects.all().order_by('-date')[:6]
    viets = Viet.objects.all().order_by('-date')[:6]
    


    return render(request, 'category/category.html', {
        'categories': categories,
        'rocks': rocks,
        'edms': edms,
        'ballads': ballads,
        'hipraps':hipraps,
        'viets': viets,

    })

def category_all(request):
    categories = Category.objects.all().order_by('-date')
    next_url = request.GET.get('next', '/category/')
    return render(request, 'category/category_all.html', {
        'categories': categories,
        'next_url': next_url
    })

def category_detail(request, id):
    category_item = get_object_or_404(Category, id=id)
    next_url = request.GET.get('next', '/category/')

    is_downloaded = False
    is_favorited = False
    if request.user.is_authenticated:
        is_downloaded = UserMusic.objects.filter(user=request.user, source_id=category_item.id, source_type='category', type='download').exists()
        is_favorited = UserMusic.objects.filter(user=request.user, source_id=category_item.id, source_type='category', type='favorite').exists()

    return render(request, 'category/category_detail.html', {
        'item': category_item,
        'is_downloaded': is_downloaded,
        'is_favorited': is_favorited,
        'next_url': next_url,
        'type': 'category',
    })

def rock_detail(request, id):
    rock_item = get_object_or_404(Rock, id=id)
    next_url = request.GET.get('next', '/category/')
    is_downloaded = False
    is_favorited = False
    if request.user.is_authenticated:
        is_downloaded = UserMusic.objects.filter(user=request.user, source_id=rock_item.id, source_type='rock', type='download').exists()
        is_favorited = UserMusic.objects.filter(user=request.user, source_id=rock_item.id, source_type='rock', type='favorite').exists()

    return render(request, 'category/category_detail.html', {
        'item': rock_item,
        'is_downloaded': is_downloaded,
        'is_favorited': is_favorited,
        'next_url': next_url,
        'type': 'rock',
    })

def rock_all(request):
    rocks = Rock.objects.all().order_by('-date')
    next_url = request.GET.get('next', '/category/')
    return render(request, 'category/rock_all.html', {'rocks': rocks, 'next_url': next_url})

def edm_detail(request, id):
    edm_item = get_object_or_404(Edm, id=id)
    next_url = request.GET.get('next', '/category/')
    is_downloaded = False
    is_favorited = False
    if request.user.is_authenticated:
        is_downloaded = UserMusic.objects.filter(user=request.user, source_id=edm_item.id, source_type='edm', type='download').exists()
        is_favorited = UserMusic.objects.filter(user=request.user, source_id=edm_item.id, source_type='edm', type='favorite').exists()

    return render(request, 'category/category_detail.html', {
        'item': edm_item,
        'is_downloaded': is_downloaded,
        'is_favorited': is_favorited,
        'next_url': next_url,
        'type': 'edm',
    })

def edm_all(request):
    edms = Edm.objects.all().order_by('-date')
    next_url = request.GET.get('next', '/category/')
    return render(request, 'category/edm_all.html', {'edms': edms, 'next_url': next_url})

def ballad_detail(request, id):
    ballad_item = get_object_or_404(Ballad, id=id)
    next_url = request.GET.get('next', '/category/')
    is_downloaded = False
    is_favorited = False
    if request.user.is_authenticated:
        is_downloaded = UserMusic.objects.filter(user=request.user, source_id=ballad_item.id, source_type='ballad', type='download').exists()
        is_favorited = UserMusic.objects.filter(user=request.user, source_id=ballad_item.id, source_type='ballad', type='favorite').exists()

    return render(request, 'category/category_detail.html', {
        'item': ballad_item,
        'is_downloaded': is_downloaded,
        'is_favorited': is_favorited,
        'next_url': next_url,
        'type': 'ballad',
    })

def ballad_all(request):
    ballads = Ballad.objects.all().order_by('-date')
    next_url = request.GET.get('next', '/category/')
    return render(request, 'category/ballad_all.html', {'ballads': ballads, 'next_url': next_url})


def viet_detail(request, id):
    viet_item = get_object_or_404(Viet, id=id)
    next_url = request.GET.get('next', '/category/')
    is_downloaded = False
    is_favorited = False
    if request.user.is_authenticated:
        is_downloaded = UserMusic.objects.filter(user=request.user, source_id=viet_item.id, source_type='viet', type='download').exists()
        is_favorited = UserMusic.objects.filter(user=request.user, source_id=viet_item.id, source_type='viet', type='favorite').exists()

    return render(request, 'category/category_detail.html', {
        'item': viet_item,
        'is_downloaded': is_downloaded,
        'is_favorited': is_favorited,
        'next_url': next_url,
        'type': 'viet',
    })

def viet_all(request):
    viets = Viet.objects.all().order_by('-date')
    next_url = request.GET.get('next', '/category/')
    return render(request, 'category/viet_all.html', {'viets': viets, 'next_url': next_url})

def hiprap_detail(request, id):
    hiprap_item = get_object_or_404(Hiprap, id=id)
    next_url = request.GET.get('next', '/category/')
    is_downloaded = False
    is_favorited = False
    if request.user.is_authenticated:
        is_downloaded = UserMusic.objects.filter(user=request.user, source_id=hiprap_item.id, source_type='hiprap', type='download').exists()
        is_favorited = UserMusic.objects.filter(user=request.user, source_id=hiprap_item.id, source_type='hiprap', type='favorite').exists()

    return render(request, 'category/category_detail.html', {
        'item': hiprap_item,
        'is_downloaded': is_downloaded,
        'is_favorited': is_favorited,
        'next_url': next_url,
        'type': 'hiprap',
    })

def hiprap_all(request):
    hipraps = Hiprap.objects.all().order_by('-date')
    next_url = request.GET.get('next', '/category/')
    return render(request, 'category/hiprap_all.html', {'hipraps': hipraps, 'next_url': next_url})