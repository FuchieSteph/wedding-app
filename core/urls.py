from django.contrib import admin
from django.urls import include, path, re_path
from suppliers.views import index
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from rest_framework import routers, serializers, viewsets
from .views import *

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('i18n/', include('django.conf.urls.i18n')), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT, show_indexes=True)

if settings.ENV == 'DEV':
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),
    ]

urlpatterns += i18n_patterns (
    path('', index, name='homepage'),
    path('suppliers/', include('suppliers.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls'), name="account"),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if 'rosetta' in settings.INSTALLED_APPS and settings.ENV == 'DEV':
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]