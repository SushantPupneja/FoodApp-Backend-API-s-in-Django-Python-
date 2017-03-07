from django.conf.urls import url, include


from .views import AppUserListAPIView , AppUserCreateAPIView

urlpatterns = [
    url(r'^$', AppUserListAPIView.as_view()),
    url(r'^create/$', AppUserCreateAPIView.as_view()),
]