from django.contrib.auth.models import User
from django.db import models

from commerce.models.base_model import BaseModel
from commerce.models.book import Book


class Cart(BaseModel):
    """ Class represents a user's cart item """
    book = models.ForeignKey(Book, null=True, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
