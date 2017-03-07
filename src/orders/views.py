from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Order
from AppUsers.models import AppUser
from products.models import Product
from django.views.decorators.csrf import csrf_exempt
# from product.models import Product
# Create your views here.


@csrf_exempt
def placeorder(request):
	total = 0
	try:
		order_details = json.loads(request.read())
		order_by_user_id = order_details["order_by_user_id"]
		order_amount = order_details["order_amount"]
		product_id = order_details["product_details"]["product_id"]
		product_qty = order_details["product_details"]["qty"]

	except Exception as e:
		print str(e)

	# order_by_user_id = request.GET.get('order_by_user_id')
	# total_order_amount = request.GET.get('order_value')
	# order_product_dic = request.GET.get('product_details')
	try:
		product_ordered = Product.objects.get(product_id=product_id) #recive product object from id, id we get in key of dic
		product_price = product_ordered.price
		total += product_price * int(product_qty)
	except Exception as e:
		print str(e)

	order_by = AppUser.objects.get(user_id=order_by_user_id) #receive Appuser object

	try:
		if total==order_amount:
			place_order = Order.objects.create(order_placed_by=order_by, order_amount=order_amount)
			place_order.save()
			responseCode = 200
			message = 'Order placed succesfully'
			order_placed_id = Order.objects.filter(order_placed_by=order_by_user_id).order_by('order_time').last().order_id
			placed_order = Order.objects.get(order_id=order_placed_id)
			placed_order.order_status = 'Confirmed'
			placed_order.save()
		else:
			responseCode = 300
			message = 'Order amount is wrong'
			order_placed_id = 0

	except Exception as e:
		print str(e)
		responseCode = 500
		message = 'Order is not placed'
		order_placed_id = 0

	
	return JsonResponse({'responseCode':responseCode, 'message':message, 'order-id':order_placed_id})
