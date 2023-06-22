from rest_framework import serializers
from ecommerce.models import Users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        exclude = ('password', 'reset_password_token', 'reset_password_expiry')
