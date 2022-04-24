import re
from rest_framework import serializers
from .models import CustomUser
from inventory.models import *
from order.models import *


def isValid(s):
    Pattern = re.compile("(0)?[7-8][0-9]{9}")
    return Pattern.match(s)


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

    def validate_phone(self, value):
        if not isValid(value):
            raise serializers.ValidationError(
                "phone number must starts with 07/08 and be 11 digit"
            )
        return value
