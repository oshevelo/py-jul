from django.test import TestCase

from .models import Product

class ProductModelTest(TestCase):
    def test_name(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')