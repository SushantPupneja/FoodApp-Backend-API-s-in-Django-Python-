from __future__ import unicode_literals

from django.db import models

from AppUsers.models import AppUser

# Create your models here.

class Order(models.Model):
	order_id = models.AutoField(primary_key=True)
	order_time = models.DateTimeField(auto_now=False, auto_now_add=True)
	order_products = models.CharField(max_length=250, null=True , blank=True)
	order_amount = models.IntegerField(null=False, blank=False)
	status_choices= (('Pending','Pending'),('Confirmed','Confirmed'),('Cancelled','Cancelled'),('Completed','Completed'))
	order_status = models.CharField(max_length=120, choices=status_choices, default='Pending')
	order_placed_by = models.ForeignKey(AppUser, on_delete=models.CASCADE)
	


	def __unicode__(self):
		return str(self.order_id)




