from django.shortcuts import render
from django.http import JsonResponse

from .models import Product
# Create your views here.

def productlist(request):
	try:
		product_list = Product.objects.all()
		data = []
		for x in product_list:
			jsonObject = {}
			jsonObject['title'] = x.title
			jsonObject['discription'] = x.discription
			jsonObject['price'] = x.price
			jsonObject['id'] = x.product_id
			jsonObject['image'] = "media/" + str(x.image)
			data.append(jsonObject)
		responseCode = 200
	except Exception as e:
		print str(e)
		product_list=[]
		responseCode = 500

	return JsonResponse({'responseCode':responseCode, 'productlist': data })

def productdetail(request,id):
	try:
		product_detail = Product.objects.get(product_id=id)
		data = []
		jsonObject = {}
		jsonObject['title'] = product_detail.title
		jsonObject['discription'] = product_detail.discription
		jsonObject['price'] = product_detail.price
		jsonObject['image'] = "media/" + str(product_detail.image)
		data.append(jsonObject)
		responseCode = 200
	except Exception as e:
		print str(e)
		responseCode = 500
	

	return JsonResponse({'responseCode':responseCode, 'product_detail':data})



