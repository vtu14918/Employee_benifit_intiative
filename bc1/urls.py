from django.contrib import admin
from django.urls import path
from.views import home,upload
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('upload/',upload),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)