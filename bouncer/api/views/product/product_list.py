from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from ...serializers.product_serializer import ProductSerializer
from ...models.product import Product

from rest_framework.pagination import PageNumberPagination
import math

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'total_count': self.page.paginator.count,
            'page_size': self.page_size,
            'page_count': math.ceil(self.page.paginator.count / self.page_size),
            'current_page': self.page.number,
            'next_link': self.get_next_link(),
            'previous_link': self.get_previous_link(),
            'results': data,
        })


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination
