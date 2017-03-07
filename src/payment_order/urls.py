from django.conf.urls import url
from .views import payment_order


urlpatterns = [
	url(r'^payment-order/$', payment_order, name='payment-request'),

	]