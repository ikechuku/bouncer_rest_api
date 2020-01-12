from rest_framework import serializers
from ..models.vendor import Vendor


class VendorSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Vendor
        fields = '__all__'
        
