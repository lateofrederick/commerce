from django.contrib.auth.models import User, Group
from django.db import models
from django.utils.crypto import get_random_string

from commerce.models.base_model import BaseModel
from commerce.utils.shortcuts import get_object_or_none


class UserProfile(BaseModel):
    SELLER = "Seller"
    BUYER = "Buyer"

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    @classmethod
    def create_user(cls, username, first_name, last_name, user_role, email=None, password=None):
        user_password = get_random_string(length=10) if password is None else password
        user_group = get_object_or_none(Group, name=user_role)

        if user_group:
            user = User(username=username, first_name=first_name, last_name=last_name, email=email)
            user.set_password(user_password)
            user.save()

            user_group.user_set.add(user)
            user_profile = cls.objects.create(user=user)
            return user_profile, user_password
        else:
            raise KeyError(f'User group {user_role} not found')

