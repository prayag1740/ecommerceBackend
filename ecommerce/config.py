class Config:

    class GENERIC:
        FAILURE = (500, "API Failed")
        AUTH_TOKEN_MISSING = (1, "Auth Token is missing")
        INVALID_TOKEN = (2, "Authorization failed")

    class PRODUCT:
        DOES_NOT_EXIST = (1, "Product does not exist")

    class USER:
        DOES_NOT_EXIST = (1, "User does not exist")
        LOGIN_INFO_MISSING = (2, "Please enter both email and password")
        INVALID_ROLE = (3, "Invalid Role . Cannot Login into system")
        USER_ID_MISSING = (4, "User ID is missing")

        