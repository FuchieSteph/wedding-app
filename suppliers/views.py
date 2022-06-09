from gettext import gettext
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Category, Supplier
from .filters import SupplierFilter

def index(request):
    categories = Category.objects.filter(parent_id__isnull=True)
    return render(request, 'categories/index.html', context={'categories':categories})

def CategoryDetailView(request, slug, pk):
    categories = Category.objects.add_related_count(Category.objects.all(), Supplier, 'category_id', 'count', cumulative=True) 
    category = Category.objects.get(pk=pk)
    sub_categories = Category.objects.filter(parent_id=pk)

    suppliers_list = Supplier.objects.filter(Q(category_id=pk)).order_by('name')
    supplier_filter = SupplierFilter(request.GET, queryset=suppliers_list)
    
    paginator = Paginator(supplier_filter.qs, 12) 
    page_number = request.GET.get('page')
    suppliers_page = paginator.get_page(page_number)

    queries_without_page = request.GET.copy()

    if queries_without_page.__contains__('page'):
        del queries_without_page['page']

    return render(request, 'list.html', {'queries': queries_without_page, 'suppliers_filters' : supplier_filter, 'categories' : categories, 'category': category, 'subcategories': sub_categories, 'suppliers': suppliers_page })

def SupplierView(request, slug, pk):
    return render(request, 'details.html', {'supplier': Supplier.objects.get(pk=pk) })