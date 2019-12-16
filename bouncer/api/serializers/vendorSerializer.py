import sys
sys.path.append('..')
from rest_framework import serializers

from ..models.user.vendor import Vendor

class VendorSerializers(serializers.ModelSerializer):
    

    class Meta:
        model = Vendor
        fields = '__All__'
