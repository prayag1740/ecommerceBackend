from django.core.validators import MaxValueValidator
from django.db import models

# Create your models here.

class Products (models.Model):

    CATEGORY_CHOICES = [
        (1, "Electronics"),
        (2, "Clothes"),
        (3, "Food"),

    ]

    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    ratings = models.IntegerField(default=0)
    images = models.JSONField()
    category = models.IntegerField(choices=CATEGORY_CHOICES, default=CATEGORY_CHOICES[0][0], null=False, blank=False)
    stock = models.IntegerField(default=1, validators=[MaxValueValidator(1000)])
    num_of_reviews = models.IntegerField(default=0)
    reviews = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'


class Users (models.Model):

    USER_ROLES = [
        ("ADMIN", 'admin'),
        ("USER", 'user')
    ]

    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(null=False, blank=False, unique=True)
    password = models.CharField(max_length=255, null=False, blank=False)
    avatar = models.JSONField(default={})
    role = models.CharField(max_length=255, null=False, blank=False, choices=USER_ROLES, default=USER_ROLES[1][0])
    reset_password_token = models.CharField(max_length=255)
    reset_password_expiry = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'





