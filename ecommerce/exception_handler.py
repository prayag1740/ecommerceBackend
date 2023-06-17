from collections import defaultdict
from rest_framework import status, exceptions
from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler
from ecommerce.config import Config


class CustomException(APIException):

    status_map = defaultdict(lambda: status.HTTP_500_INTERNAL_SERVER_ERROR)

    status_map[400] = status.HTTP_400_BAD_REQUEST
    status_map[401] = status.HTTP_401_UNAUTHORIZED
    status_map[403] = status.HTTP_403_FORBIDDEN
    status_map[404] = status.HTTP_404_NOT_FOUND
    status_map[405] = status.HTTP_405_METHOD_NOT_ALLOWED
    status_map[406] = status.HTTP_406_NOT_ACCEPTABLE
    status_map[409] = status.HTTP_409_CONFLICT

    def __init__(self, code, response=None):

        self.status_code = self.status_map[code]

        if not response:
            response = Config.GENERIC.FAILURE

        super().__init__(response)
