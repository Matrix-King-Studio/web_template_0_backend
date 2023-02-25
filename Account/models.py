from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class User(AbstractUser):
    openid = models.CharField(
        verbose_name="微信登录用户唯一标识",
        max_length=128,
        unique=True,
        null=True,
        blank=True,
        help_text="普通用户的标识，对当前开发者帐号唯一"
    )
    unionId = models.CharField(
        verbose_name="微信登录用户统一标识",
        max_length=128,
        unique=True,
        null=True,
        blank=True,
        help_text="针对一个微信开放平台帐号下的应用，同一用户的unionid是唯一的。"
    )

    objects = UserManager()
