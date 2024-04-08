from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns

from . import settings


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    ]+i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path('users/', include('users.urls')),
    path('', include('catalog.urls')),
    prefix_default_language=False
)




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
