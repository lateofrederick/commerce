from django.contrib.auth.models import User
from django.db import models

from commerce.models.base_model import BaseModel
from commerce.models.book import Book


class Order(BaseModel):
    book = models.ForeignKey(Book, null=True, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
