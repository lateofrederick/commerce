from django.db import models
from cloudinary.models import CloudinaryField

from commerce.models.base_model import BaseModel


class Book(BaseModel):
    title = models.CharField(max_length=60, null=False, blank=False)
    description = models.CharField(max_length=2000, null=True, blank=True)
    author = models.CharField(max_length=255, null=False, blank=False)
    price = models.IntegerField(default=0)
    image = CloudinaryField('image')
