from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from core.helpers import RandomFileName 

# Create your models here.
class Category(MPTTModel):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    slug = models.CharField(max_length=200, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    icon = models.ImageField(upload_to=RandomFileName('categories-icons'), blank=True)

    def __str__(self):
        return self.name

class Supplier(models.Model):
    PRICE_RANGE = (
        ('€', '€'),
        ('€€', '€€'),
        ('€€€', '€€€'),
    )
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    slug = models.CharField(max_length=200)
    image = models.ImageField(upload_to=RandomFileName('suppliers'), blank=True)
    url = models.CharField(max_length=200)
    price_range = models.CharField(max_length=200, blank=True, choices=PRICE_RANGE)
    adress = models.CharField(max_length=200, blank=True)
    postal_code = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)
    caterer_free = models.BooleanField()
    brewer_free = models.BooleanField()
    furnitures_included = models.BooleanField()
    dishes_included = models.BooleanField()
    gite_included = models.BooleanField()
    corkage_fee = models.BooleanField()
    buffet = models.BooleanField()
    echoppes = models.BooleanField()
    menu = models.BooleanField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

