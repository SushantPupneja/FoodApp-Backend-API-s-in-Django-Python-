from django.conf.urls import url
from .views import placeorder


urlpatterns = [
	url(r'^place-order/$', placeorder, name='order'),

	]

 # url(r'^products/$', productlist , name='list'),