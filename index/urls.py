from django.urls import path
from . import views

app_name ='index'
urlpatterns = [
    path('', views.index, name='index'),

    # Music
    path('music/', views.music_all, name='music_all'),
    path('music/<int:id>/', views.music_detail, name='music_detail'),

    # Hot
    path('hot/', views.hot_all, name='hot_all'),
    path('hot/<int:id>/', views.musichot_detail, name='musichot_detail'),

    path('download/<str:type>/<int:id>/', views.add_download, name='add_download'),
    path('favorite/<str:type>/<int:id>/', views.add_favorite, name='add_favorite'),
    path('remove-download/<str:type>/<int:id>/', views.remove_download, name='remove_download'),
    path('remove-favorite/<str:type>/<int:id>/', views.remove_favorite, name='remove_favorite'),
    # path("search/", views.search, name="search"),
]
