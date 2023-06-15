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


class BaseProduct(APIView):

    def post(self, request, *args, **kwargs):
    
        request_data = request.data
        serializer = ProductSerializer(data= request_data)
        if not serializer.is_valid():
            response = {"error" : serializer.errors}
            return Response(response, status=http_status.HTTP_400_BAD_REQUEST)

        product = Products.objects.create(**request_data)
        serializer = ProductSerializer(product).data
        
        return Response(serializer, status=http_status.HTTP_200_OK)

    def get(self, request, id):
    
        try:
            prod = Products.objects.get(id=id)
        except Products.DoesNotExist:
            resp = {"error" : "Product does not exist"}
            return Response(resp, status=http_status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(prod).data
        return Response(serializer, status=http_status.HTTP_200_OK)

    def put(self, request, id):
        try:
            prod = Products.objects.get(id=id)
        except Products.DoesNotExist:
            resp = {"error" : "Product does not exist"}
            return Response(resp, status=http_status.HTTP_404_NOT_FOUND)

        prod.__dict__.update(request.data)
        prod.save()
        serializer = ProductSerializer(prod).data

        return Response(serializer, status=http_status.HTTP_200_OK)

    def delete(self, request, id):

        try:
            prod = Products.objects.get(id=id)
        except Products.DoesNotExist:
            resp = {"error" : "Product does not exist"}
            return Response(resp, status=http_status.HTTP_404_NOT_FOUND)

        prod.delete()
        resp = {"message" : "success"}
        return Response(resp, status=http_status.HTTP_200_OK)








        




        
        