class Config:

    class GENERIC:
        FAILURE = (500, "API Failed")

    class PRODUCT:
        DOES_NOT_EXIST = (1, "Product does not exist")

    class USER:
        DOES_NOT_EXIST = (1, "User does not exist")
        LOGIN_INFO_MISSING = (2, "Please enter both email and password")

        