from ...models.product import Product
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from ...models.vendor import Vendor
from ...models.category import Category
from ...serializers.product_serializer import ProductSerializer

"""
This function gets the product imformation of a specified product
product_id (string)
Returns:
    Response (object) with
        message - Product details fetched successfully
        product - {}
"""
class GetProductDetails(APIView):
    def post(self, request):
        data = request.data
        product_id = data["id"]

        try:
            product = Product.objects.get(id=product_id)
            vendor = product.category_id
            category = product.vedor_id

            serialized_product = ProductSerializer(product)
            serialized_vendor = ProductSerializer(vendor)
            serialized_category = ProductSerializer(category)
            
            
            return Response({
                "product": serialized_product.data,
                "product_vendor": serialized_vendor,
                "category": serialized_category
            }, status=status.HTTP_200_OK)

        except:
            return Response({"message":"This product was not found"}, status=status.HTTP_400_BAD_REQUEST)

 