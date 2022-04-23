from rest_framework import serializers
from .models import CustomUser
from inventory.models import *
from order.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "url",
            "username",
            "email",
            "phone",
            "first_name",
            "last_name",
            "address",
            "address_2",
        ]
        read_only = True
        editable = False
