import sys
sys.path.append('..')
from rest_framework import serializers

from ..models.customers import Customers

class CustomerSerializers(serializers.ModelSerializer):
    

    class Meta:
        model = Customers
        fields = '__All__'
