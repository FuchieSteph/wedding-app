import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.dev")

import django 
django.setup() 

from faker import factory,Faker 
from suppliers.models import * 
from model_bakery.recipe import Recipe,foreign_key 

fake = Faker() 
categorie_tree = Category.objects.order_by('-tree_id')[0]
categories_id = Category.objects.all().values_list('id', flat=True)

for k in range(1000):
    category=Recipe(Category,
                name=fake.word(),
                slug=fake.word(),
                description=fake.text(),
                icon='categories-icons/90748d67-5549-435e-b22b-8e22545d6fe7.png',
                lft=1,
                rght=2,
                tree_id=categorie_tree.tree_id + 1 + k,
                level=0,
                parent_id=fake.random_element(elements=categories_id),
                )
    #category.make()

    supplier=Recipe(Supplier,
                name=fake.company(),
                slug=fake.word(),
                description=fake.text(),
                image= fake.image_url(width=1000, height=600, placeholder_url='https://placeimg.com/{width}/{height}?random='+str(k)),
                type=fake.random_element(elements=('caterer', 'reception', 'other')),
                price_range=fake.random_element(elements=('€', '€€', '€€€')),
                adress=fake.address(),
                city=fake.city(),
                country=fake.country(),
                postal_code=fake.postcode(),
                caterer_free=fake.boolean(chance_of_getting_true=50),
                furnitures_included=fake.boolean(chance_of_getting_true=50),
                dishes_included=fake.boolean(chance_of_getting_true=50),
                gite_included=fake.boolean(chance_of_getting_true=50),
                corkage_fee=fake.boolean(chance_of_getting_true=50),
                buffet=fake.boolean(chance_of_getting_true=50),
                echoppes=fake.boolean(chance_of_getting_true=50),                
                menu=fake.boolean(chance_of_getting_true=50),   
                category_id=fake.random_element(elements=categories_id),
    )
    supplier.make()
print('ok')