from __future__ import unicode_literals

from django.db import models

# Create your models here.

def upload_location(instance, filename):
	ProductModel = instance.__class__
	if ProductModel.objects.order_by("product_id").last().product_id:
		new_id = ProductModel.objects.order_by("product_id").last().product_id
	return "myimages/%s%s" %(new_id, filename)

"""
    instance.__class__ gets the model Post. We must use this method because the model is defined below.
    Then create a queryset ordered by the "id"s of each object, 
    Then we get the last object in the queryset with `.last()`
    Which will give us the most recently created Model instance
    We add 1 to it, so we get what should be the same id as the the post we are creating.

"""


class Product(models.Model):
	product_id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=50, null=False)
	discription = models.TextField(max_length=50, null=True)
	image = models.ImageField(
            upload_to=upload_location, 
            null=True, 
            blank=True, 
            width_field="width_field", 
            height_field="height_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	price = models.IntegerField(default=0)

	def __str__(self):
		return self.product_id