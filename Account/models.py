from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class Account(AbstractBaseUser):
	openid = models.CharField(max_length=64, unique=True)
	unionId = models.CharField(max_length=64, unique=True)
	nickname = models.CharField(max_length=64)
	headImgUrl = models.URLField()

	USERNAME_FIELD = "openid"

	def get_username(self):
		return self.nickname

	@property
	def username(self):
		return self.nickname
