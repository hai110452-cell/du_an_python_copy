# exclusive/urls.py
from django.urls import path
from . import views
from .views import ExclusiveItemUploadAPI

app_name = 'exclusive'

urlpatterns = [
    path('', views.home, name='home'),
    path('all/', views.all_items, name='all'),
    path('<int:pk>/', views.exclusive_detail, name='detail'),
    path('download/<str:type>/<int:id>/', views.add_download, name='add_download'),
    path('favorite/<str:type>/<int:id>/', views.add_favorite, name='add_favorite'),
    path('remove-download/<str:type>/<int:id>/', views.remove_download, name='remove_download'),
    path('remove-favorite/<str:type>/<int:id>/', views.remove_favorite, name='remove_favorite'),

    path('api/exclusive/upload/', ExclusiveItemUploadAPI.as_view(), name='viet-upload'),
]