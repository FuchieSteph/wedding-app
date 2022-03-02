from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
class Category(MPTTModel):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    slug = models.CharField(max_length=200, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    icon = models.ImageField(upload_to='categories/icons', blank=True)
    background =  models.ImageField(upload_to='categories/background', blank=True)
    filters_fields = models.TextField(default='', blank=True)

    def __str__(self):
        return self.name

class Provider(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    slug = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    price_range = models.CharField(max_length=200, blank=True)
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
