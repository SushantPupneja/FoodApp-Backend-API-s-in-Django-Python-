from .serializers import AppUserListAPISerializer , AppUserCreateAPISerializer

from rest_framework.generics import (
	CreateAPIView,
	ListAPIView,
	# UpdateAPIView,
	# DestroyAPIView, 
	# RetrieveAPIView,
	# RetrieveUpdateAPIView,
	)

from AppUsers.models import AppUser

class AppUserListAPIView(ListAPIView):
	queryset = AppUser.objects.all()
	serializer_class = AppUserListAPISerializer

class AppUserCreateAPIView(CreateAPIView):
	queryset = AppUser.objects.all()
	serializer_class = AppUserCreateAPISerializer

		