from __future__ import unicode_literals

from django.db import models

from orders.models import Order
from AppUsers.models import AppUser

# Create your models here.

class Payment_Order(models.Model):
	payment_order_receipt_no = models.CharField(max_length=30)
	entity = models.CharField(max_length=10, default='Payment')
	amount = models.IntegerField()
	currency = models.CharField(max_length=20, default='INR')
	status_choices= (('created','created'),('authorized','authorized'),('captured','captured'),
					('refunded','refunded'),('failed','failed'))
	status = models.CharField(choices=status_choices, default='created', max_length=20)
	method_choices= (('card','card'),('netbanking','netbanking'),
					('wallet','wallet'),('emi','emi'))
	method = models.CharField(max_length=20, default='Card', choices=method_choices)
	order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
	user_id = models.ForeignKey(AppUser, on_delete=models.CASCADE)
	description = models.CharField(max_length=100, default='None')
	international = models.BooleanField(default=False)
	razorpay_order_id = models.CharField(max_length=50, default='NA', null=False, blank=False)
	refund_choices = (('null','null'),('partial','partial'),('full','full'))
	refund_status = models.CharField(max_length=20, default='null', choices=refund_choices)
	amount_refunded = models.IntegerField(default=0)
	captured = models.BooleanField(default=False)
	fee = models.IntegerField(default=0)
	service_tax = models.IntegerField(default=0)
	error_code = models.CharField(max_length=20, default='None')
	error_description = models.CharField(max_length=50, default='None')
	created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
	last_update = models.DateTimeField(auto_now=True, auto_now_add=False)


	def __str__(self):
		return self.payment_order_receipt_no




	
