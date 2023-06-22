import requests
from ecommerce.models import Products, Users
from ecommerce.serializers.product import ProductSerializer
from ecommerce.serializers.user import UserSerializer
from ecommerce.controllers.product import ProductController
from ecommerce.controllers.user import UserController
from rest_framework import status as http_status
from rest_framework.views import APIView
from ecommerce.exception_handler import CustomException
from django.core.paginator import Paginator
from django.contrib.auth.hashers import make_password
from ecommerce.config import Config
from ecommerce.constants import PAGE_LIMIT
from rest_framework.response import Response

# Create your views here.

class GetProducts(APIView):

    def get(self, request, *args, **kwargs):

        products = Products.objects.all()
        product_count = products.count()
        query_params = request.query_params
        page_number = query_params.get('page', 1)
        products = ProductController().search_and_filter_products(query_params.copy(), products)
        paginator = Paginator(products, per_page=PAGE_LIMIT) 
        page_obj = paginator.get_page(page_number)  
        serializer = ProductSerializer(page_obj.object_list, many=True).data

        response = {"status" : 0, "data" : serializer, "count" : product_count}

        return Response(response, status=http_status.HTTP_200_OK)


class BaseProduct(APIView):

    def post(self, request, *args, **kwargs):
    
        request_data = request.data
        serializer = ProductSerializer(data= request_data)
        if not serializer.is_valid():
            response = {"status" : 1, "error" : serializer.errors}
            raise CustomException(http_status.HTTP_400_BAD_REQUEST, response)

        product = Products.objects.create(**request_data)
        serializer = ProductSerializer(product).data
        
        return Response(serializer, status=http_status.HTTP_200_OK)

    def get(self, request, id):
    
        try:
            prod = Products.objects.get(id=id)
        except Products.DoesNotExist:
            error_code = Config.PRODUCT.DOES_NOT_EXIST
            resp = {"status" : error_code[0], "message" : error_code[1] }
            raise CustomException(http_status.HTTP_404_NOT_FOUND, resp)
            
        serializer = ProductSerializer(prod).data
        return Response(serializer, status=http_status.HTTP_200_OK)

    def put(self, request, id):
        try:
            prod = Products.objects.get(id=id)
        except Products.DoesNotExist:
            error_code = Config.PRODUCT.DOES_NOT_EXIST
            resp = {"status" : error_code[0], "message" : error_code[1] }
            raise CustomException(http_status.HTTP_404_NOT_FOUND, resp)

        prod.__dict__.update(request.data)
        prod.save()
        serializer = ProductSerializer(prod).data

        return Response(serializer, status=http_status.HTTP_200_OK)

    def delete(self, request, id):

        try:
            prod = Products.objects.get(id=id)
        except Products.DoesNotExist:
            error_code = Config.PRODUCT.DOES_NOT_EXIST
            resp = {"status" : error_code[0], "message" : error_code[1] }
            raise CustomException(http_status.HTTP_404_NOT_FOUND, resp)

        prod.delete()
        resp = {"message" : "success"}
        return Response(resp, status=http_status.HTTP_200_OK)


class User (APIView):

    def post(self, request):

        request_data = request.data
        serializer = UserSerializer(data=request_data)

        try:
            if not serializer.is_valid():
                response = {"status" : 1, "error" : serializer.errors}
                raise CustomException(http_status.HTTP_400_BAD_REQUEST, response)
        except Exception as e:
            print(e.__traceback__)
            err_code = Config.GENERIC.FAILURE
            resp = {"status" : err_code[0], "message" : err_code[1]}
            return Response(resp, status=http_status.HTTP_500_INTERNAL_SERVER_ERROR)

        name = request_data["name"]
        email = request_data["email"]
        pass_encrypted = make_password(request_data["password"])
        avatar = request_data.get("avatar", {})
        role = request_data.get("role", Users.USER_ROLES[1][0])

        user = Users.objects.create(name=name, email=email, password=pass_encrypted, avatar=avatar, role=role)
        jwt_token = UserController.create_jwt_token(user.id)
            
        serializer = UserSerializer(user).data
        serializer["token"] = jwt_token
        
        return Response(serializer, status=http_status.HTTP_200_OK)




        








        




        
        