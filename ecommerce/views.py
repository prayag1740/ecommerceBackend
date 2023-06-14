import requests
from ecommerce.models import Products
from .serializers.product import ProductSerializer
from rest_framework import status as http_status
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class GetProducts(APIView):

    def get(self, request, *args, **kwargs):

        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True).data

        response = {"data" : serializer}

        return Response(response, status=http_status.HTTP_200_OK)


class CreateProduct(APIView):

    def post(self, request, *args, **kwargs):

        request_data = request.data
        serializer = ProductSerializer(data= request_data)
        if not serializer.is_valid():
            response = {"error" : serializer.errors}
            return Response(response, status=http_status.HTTP_400_BAD_REQUEST)

        product = Products.objects.create(**request_data)
        serializer = ProductSerializer(product).data
        response = serializer

        return Response(response, status=http_status.HTTP_200_OK)
