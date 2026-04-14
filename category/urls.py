from django.urls import path
from . import views
from .views import CategoryUploadAPI, BalladUploadAPI, EdmUploadAPI, RockUploadAPI, HiprapUploadAPI, VietUploadAPI

app_name = 'category'

urlpatterns = [
    path('', views.category_list, name='category'),
    path('category_all/', views.category_all, name='category_all'),
    path('detail/<int:id>/', views.category_detail, name='category_detail'),

    path('ballad_all/', views.ballad_all, name='ballad_all'),
    path('ballad_detail/<int:id>/', views.ballad_detail, name='ballad_detail'),

    path('edm_all/', views.edm_all, name='edm_all'),
    path('edm_detail/<int:id>/', views.edm_detail, name='edm_detail'),

    path('rock_all/', views.rock_all, name='rock_all'),
    path('rock_detail/<int:id>/', views.rock_detail, name='rock_detail'),

    path('hiprap_all/', views.hiprap_all, name='hiprap_all'),
    path('hiprap_detail/<int:id>/', views.hiprap_detail, name='hiprap_detail'),

    path('viet_all/', views.viet_all, name='viet_all'),
    path('viet_detail/<int:id>/', views.viet_detail, name='viet_detail'),
    path('add_download/<str:type>/<int:id>/', views.add_download, name='add_download'),
    path('add_favorite/<str:type>/<int:id>/', views.add_favorite, name='add_favorite'),
    path('remove_download/<str:type>/<int:id>/', views.remove_download, name='remove_download'),
    path('remove_favorite/<str:type>/<int:id>/', views.remove_favorite, name='remove_favorite'),

    path('api/category/upload/', CategoryUploadAPI.as_view(), name='category-upload'),
    path('api/ballad/upload/', BalladUploadAPI.as_view(), name='ballad-upload'),
    path('api/edm/upload/', EdmUploadAPI.as_view(), name='edm-upload'),
    path('api/rock/upload/', RockUploadAPI.as_view(), name='rock-upload'),
    path('api/hiprap/upload/', HiprapUploadAPI.as_view(), name='hiprap-upload'),
    path('api/viet/upload/', VietUploadAPI.as_view(), name='viet-upload'),
]