# usermusic/urls.py
from django.urls import path
from . import views


app_name = 'kho'
urlpatterns = [
    path('', views.kho_list, name='kho_list'),
    path('download/', views.kho_download_all, name='kho_download_all'),
    path('favorite/', views.kho_favorite_all, name='kho_favorite_all'),
    path('<int:id>/', views.kho_detail, name='kho_detail'), 
    path('remove-download/<str:type>/<int:id>/', views.remove_download, name='remove_download'),
    path('remove-favorite/<str:type>/<int:id>/', views.remove_favorite, name='remove_favorite'),
]