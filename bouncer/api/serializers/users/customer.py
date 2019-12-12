import sys
sys.path.append('..')
from rest_framework import serializers

from ...models.user.customers import Customer

class CustomerSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Customer
        fields = '__All__'
