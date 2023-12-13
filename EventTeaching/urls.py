
from django import urls
from django.conf import settings
from EventTeaching.settings import STATIC_URL, MEDIA_URL, MEDIA_ROOT
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #path to access the app urls
    path('', include('Teachingapp.urls')),
    path('summernote/', include('django_summernote.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)




