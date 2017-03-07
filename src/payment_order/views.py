from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import razorpay
import ast
from .models import Payment_Order
from orders.models import Order
from AppUsers.models import AppUser
# Create your views here.

@csrf_exempt
def payment_order(request):

	try:
		data = json.loads(request.read())

		amount = data["amount"]
		order_id = data["order_id"] #order ID
		user_id = data["user_id"]
		payment_capture = 1
		payment_order_id = Order.objects.get(order_id=order_id)
		payment_user_id = AppUser.objects.get(user_id=user_id)
		payment_request = Payment_Order.objects.create(amount=amount, order_id=payment_order_id, user_id=payment_user_id)
		payment_request.save()
		payment_request_obj = Payment_Order.objects.filter().order_by('created_at').last()
		str_payment_request_id = str(payment_request_obj.id)
		str_order_id = str(order_id)
		receipt = "razpy00O%s_P%s" %(str_order_id,str_payment_request_id)
		payment_request_obj.payment_order_receipt_no = receipt
		payment_request_obj.save()

		try:	
			DATA = {'amount':amount,'receipt':receipt, 'payment_capture':payment_capture,'currency':'INR'}
			client = razorpay.Client(auth=("rzp_test_3nFELOr7bXJh1l", "CB4LvqKCMsURzpg64dWETiSo")) 
			razorpay_response_data = client.order.create(data=DATA)
			data_as_json = json.dumps(razorpay_response_data)
			data = json.loads(data_as_json)
			razorpay_order_id = data['id']
			payment_request_obj.razorpay_order_id = razorpay_order_id
			payment_request_obj.save()
			message = 'payment success'
			responseCode = 200
		except Exception as e:
			message = 'From Razorpay payment failed'
			payment_request_obj.status = 'failed'
			payment_request_obj.save()
			responseCode = 404
			print str(e)
			
	except Exception as e:
		message = 'payment fail'
		responseCode = 400
		razorpay_order_id = 'None'
		print str(e)

	# key_id						key_secret
	# rzp_test_3nFELOr7bXJh1l		CB4LvqKCMsURzpg64dWETiSo

	# try:
	# 	
	# 	responseCode = 200
	# 	message = "Payment is successfull against order-id %s, Payment Reference Number is %s" %(receipt, payment_order_reference_id)
	# except Exception as e:
	# 	print str(e)

	return JsonResponse({'message':message, 'responseCode':responseCode, 'razorpay order id':razorpay_order_id})
	








