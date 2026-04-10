from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('index.urls')),
    path('category/', include('category.urls')),
    path('docquyen/', include('exclusive.urls')),
    path('kho/', include('kho.urls')),
    path('register/', include('register.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)