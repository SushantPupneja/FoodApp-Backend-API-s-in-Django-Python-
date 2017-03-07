from django.conf.urls import url

from .views import create_user , change_password , login

urlpatterns = [
    
    url(r'^create-user/$', create_user, name="create_user"),
    url(r'^change-password/$', change_password , name="change-password"),
    url(r'^login/$', login , name='login'),
]