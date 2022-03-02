from gettext import gettext
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponse
from django.utils.translation import gettext as _

from .models import Category, Provider

def index(request):
    categories = Category.objects.filter(parent_id__isnull=True)
    return render(request, 'categories/index.html', context={'categories':categories})

class DetailView(generic.DetailView):
    model = Category
    template_name = 'categories/details.html'

class ProviderView(generic.DetailView):
    model = Provider
    template_name = 'categories/details.html'