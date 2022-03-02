from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'providers'
urlpatterns = [
    path('', views.index, name='index'),
    path('categories/<str:slug>/<int:pk>', views.DetailView.as_view(), name='category'),
]
