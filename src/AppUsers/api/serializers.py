from rest_framework.serializers import ModelSerializer

from AppUsers.models import AppUser


class AppUserListAPISerializer(ModelSerializer):
	class Meta:
		model = AppUser
		fields = [
			"user_id",
			"first_name",
			"last_name",
			"email",
			"password",
			"mobile_no",
	]


class AppUserCreateAPISerializer(ModelSerializer):
	class Meta:
		model = AppUser
		fields = [
			"first_name",
			"last_name",
			"email",
			"password",
			"mobile_no",
	]