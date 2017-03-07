from django.shortcuts import render
from django.http import JsonResponse
from .models import AppUser
from validate_email import validate_email
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.
@csrf_exempt
def create_user(request):
	# user_id = models.AutoField(primary_key=True)
	datas = json.loads(request.read())
	print datas
	# datas = datas["data"]
	first_name = datas["first_name"]
	last_name = datas["last_name"]
	email = datas["email"]
	password = datas["password"]
	mobile_no = datas["mobile_no"]


		# first_name = request.GET.get('first_name')
		# last_name = request.GET.get('last_name')
		# email = request.GET.get('email')
		# password = request.GET.get('password')
		# mobile_no = request.GET.get('mobile_no')

	try:
		user = AppUser.objects.create(first_name= first_name, last_name=last_name, email=email,
			  password=password, mobile_no=mobile_no)
		user.save()
		# new_user_list = AppUser.objects.filter(email=email)
		# for new_user in new_user_list:
			# new_user_id = new_user.user_id
		new_user = AppUser.objects.get(email=email)
		new_user_id = new_user.user_id
		message = "created succesfully"
		responseCode = 200
		
	except Exception as e:
		print str(e)
		message = "already a user"
		responseCode = 500
		new_user_id = 0

	return JsonResponse({'responseCode': responseCode, 'message': message, 'user id': new_user_id})

def change_password(request):
	email = request.GET.get('email')
	new_password = request.GET.get('password')
	
	try:
		user = AppUser.objects.get(email=email)
		if user:
			for u1 in user:
				u1.password = new_password
				u1.save()
		message = 'Password Changed Successfully'
		responseCode = 200
	except Exception as e:
		print str(e)
		message = "Password Not Changed! Try again."
		responseCode = 500

	return JsonResponse({'responsecode':responseCode, 'message':message})


def login(request):
	userdata = request.GET.get('userdata')
	user_password = request.GET.get('user_password')
	userdata_is_valid = validate_email(userdata)

	
	try:
		if userdata_is_valid:
			user = AppUser.objects.filter(email=userdata)
			if user:
				for ob1 in user:
					ob1.password=user_password
					user_login = True
					message = 'User is Logged in'
					responseCode=200
			else:
				user_login = False
				message = 'User is not registered with us'
				responseCode=200


		elif len(userdata) == 10 and userdata.isdigit():
			user = AppUser.objects.filter(mobile_no=userdata)
			if user:
				for ob1 in user:
					ob1.password=user_password
					user_login = True
					message = 'User is Logged in'
					responseCode=200

		else:
			user_login = False
			message = 'Please Enter valid Credintials'
			responseCode=500


	except Exception as e:
		print str(e)
		user_login = False
		message = 'Please Enter valid Credintials'
		responseCode=500

	return JsonResponse({'responseCode':responseCode, 'message':message, 'login':user_login})


