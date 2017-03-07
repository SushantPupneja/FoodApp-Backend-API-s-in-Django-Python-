from django.contrib import admin
from .models import Order
from AppUsers.models import AppUser

# Register your models here.

class OrderModelAdmin(admin.ModelAdmin):
	list_display = ["order_id", "order_placed_by" , "order_amount", "order_status" , "order_time"]
	list_editable = ["order_status"]

	class Meta:
		model = Order

admin.site.register(Order,OrderModelAdmin)