from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from .views import productlist, productdetail

urlpatterns = [
    url(r'^products/$', productlist , name='list'),
    url(r'^products/(?P<id>\d+)/$', productdetail, name='detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)