from __future__ import unicode_literals

from django.db import models

# Create your models here.
class AppUser(models.Model):
	user_id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=25, null=False)
	last_name = models.CharField(max_length=25, null=False)
	email = models.EmailField(max_length=50, null=False, unique=True)
	password = models.CharField(max_length=20, null=False)
	mobile_no = models.CharField(max_length=12, null=False)

	def __str__ (self):
		return str(self.user_id)


	