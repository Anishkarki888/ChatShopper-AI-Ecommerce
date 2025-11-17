from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def get_products(request):
    products = [
        {"id": 1, "name": "Acer Aspire 7", "price": 599, "image": "..."},
        {"id": 2, "name": "Dell Inspiron", "price": 649, "image": "..."},
    ]
    return Response(products)
