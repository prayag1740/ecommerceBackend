import  os, jwt
from ecommerce.models import Users
from ecommerce.config import Config
from ecommerce.exception_handler import CustomException
from rest_framework import status as http_status



class UserController:

    @staticmethod
    def create_jwt_token(user_id):
        
        try:
            user = Users.objects.get(pk=user_id)
        except User.DoesNotExist:
            error = Config.USER.DOES_NOT_EXIST
            resp = {"status" : error[0], "message" : error[1]}
            raise CustomException(http_status.HTTP_400_BAD_REQUEST, resp)
        
        body = {
            "id" : user_id,
            "name" : user.name,
            "email" : user.email,
            "role" : user.role,
        }
        jwt_secret_token = os.environ.get('JWT_SECRET_KEY')
        jwt_token = jwt.encode(payload=body, key=jwt_secret_token, algorithm='HS256')
        return jwt_token


        