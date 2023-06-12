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




