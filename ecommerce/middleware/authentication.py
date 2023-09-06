import jwt, os, traceback, re
from django.utils import timezone
from datetime import datetime
from rest_framework import exceptions
from django.utils.timezone import make_aware
from rest_framework import status as http_status
from ecommerce.config import Config
from ecommerce.models import Products, Users
from ecommerce.exception_handler import CustomException



class AuthMiddleWare:

    def validate_token(self, request, *args, **kwargs):

        jwt_auth_token	= request.headers.get("authorization", None)
        if not jwt_auth_token:
            error = Config.GENERIC.AUTH_TOKEN_MISSING
            response = {"status" : error[0], "message" : error[1]}
            raise CustomException(http_status.HTTP_401_UNAUTHORIZED, response)
        try:
            self.payload = jwt.decode(jwt_auth_token, os.environ.get('JWT_SECRET_KEY'), algorithms=['HS256'])
            exp = self.payload.get('exp')
            # self.check_token_expiry(exp)
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            error = Config.GENERIC.INVALID_TOKEN
            response = {"status" : error[0], "message" : error[1]}
            raise CustomException(http_status.HTTP_401_UNAUTHORIZED, response)


    @staticmethod
    def check_token_expiry(token_exp):
        if make_aware(datetime.fromtimestamp(exp_time)) <= timezone.now():
            raise exceptions.AuthenticationFailed("Token expired")





class UserAuthentication(AuthMiddleWare):

    def initial(self, request, *args, **kwargs):
        print("initial method called --> user authentication")

        self.validate_token(request)

        role = self.payload.get('role')

        if role != Users.USER_ROLES[1][0]:
            error = Config.USER.INVALID_ROLE
            response = {"status" : error[0], "message" : error[1]}
            raise CustomException(http_status.HTTP_401_UNAUTHORIZED, response)

        

class AdminAuthentication(AuthMiddleWare):
    
    def initial(self, request, *args, **kwargs):
        print("initial method called --> admin authentication")
        
        req_url = request.get_full_path()

        #bypass for get product
        regex_pattern = r"^/ecommerce/product/(\d+)$"
        if request.method == "GET" and re.match(regex_pattern, req_url):
            return

        self.validate_token(request)

        role = self.payload.get('role')

        if role != Users.USER_ROLES[0][0]:
            error = Config.USER.INVALID_ROLE
            response = {"status" : error[0], "message" : error[1]}
            raise CustomException(http_status.HTTP_401_UNAUTHORIZED, response)