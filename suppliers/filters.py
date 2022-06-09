import django_filters
from django_filters.filters import OrderingFilter
from .models import Category, Supplier

class SupplierFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    
    o = OrderingFilter(
        # tuple-mapping retains order
        fields=(
            ('name', 'name'),
            ('price_range', 'price_range'),
            ('pk', 'pk'),
        ),
    )

    class Meta:
        model = Supplier
        fields = ['name', 'city', 'country', 'caterer_free', 'brewer_free', 'furnitures_included', 'dishes_included', 'gite_included', 'corkage_fee', 'buffet', 'echoppes', 'menu', 'category', 'type', 'tag']

