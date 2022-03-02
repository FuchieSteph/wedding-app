from django.contrib import admin
from django.urls import include, path, re_path
from providers.views import index
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT, show_indexes=True)

if settings.ENV == 'DEV':
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),
    ]

urlpatterns += i18n_patterns (
    path('', index, name='homepage'),
    path('members/', include('members.urls')),
    path('providers/', include('providers.urls')),
    path('admin/', admin.site.urls)
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if 'rosetta' in settings.INSTALLED_APPS and settings.ENV == 'DEV':
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]