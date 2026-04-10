from django.shortcuts import render
from django.db.models import Q
from index.models import Music, MusicHot
from category.models import Ballad, Category,  Rock, Edm, Viet, Hiprap
from exclusive.models import ExclusiveItem

# Create your views here.
# def index(request):
#     return render(request, 'home/index.html')
# def contact(request):
#     return render(request, 'home/contact.html')
# def category(request):
#     return render(request, 'home/category.html')
# def kho(request):
#     return render(request, 'home/kho.html')
# def register(request):
#     return render(request, 'home/register.html')
def search(request):
    query = request.GET.get('q', '')

    results = []

    # App music
    music_results = Music.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query)
    )
    for item in music_results:
        results.append({
            'type': 'music',
            'obj': item,
            'url_name': 'index:music_detail'
        })

    musichot_results = MusicHot.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query)
    )
    for item in musichot_results:
        results.append({
            'type': 'musichot',
            'obj': item,
            'url_name': 'index:musichot_detail'
        })

    # App category
    ballad_results = Ballad.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query)
    )
    for item in ballad_results:
        results.append({
            'type': 'ballad',
            'obj': item,
            'url_name': 'category:ballad_detail'
        })

    rock_results = Rock.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query)
    )
    for item in rock_results:
        results.append({
            'type': 'rock',
            'obj': item,
            'url_name': 'category:rock_detail'
        })

    hiprap_results = Hiprap.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query)
    )
    for item in hiprap_results:
        results.append({
            'type': 'hiprap',
            'obj': item,
            'url_name': 'category:hiprap_detail'
        })

    category_results = Category.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query)
    )
    for item in category_results:
        results.append({
            'type': 'hiprap',
            'obj': item,
            'url_name': 'category:category_detail'
        })
    


    edm_results = Edm.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query)
    )
    for item in edm_results:
        results.append({
            'type': 'edm',
            'obj': item,
            'url_name': 'category:edm_detail'
        })



    viet_results = Viet.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query)
    )
    for item in viet_results:
        results.append({
            'type': 'viet',
            'obj': item,
            'url_name': 'category:viet_detail'
        })



    exclusive_results = ExclusiveItem.objects.filter(
    Q(title__icontains=query) | Q(content__icontains=query)
)
    for item in exclusive_results:
        results.append({
        'type': 'exclusive',
        'obj': item,
        'url_name': 'exclusive:detail'
    })

    return render(request, 'home/search.html', {
        'query': query,
        'results': results
    })

    