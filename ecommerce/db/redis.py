from django.core.cache import cache
class RedisController:

    @staticmethod
    def set_key(key, val, expires):
        if expires:
            cache.set(key, val)
        else:
            cache.set(key, val)


    @staticmethod
    def get_value(key):

        return cache.get(key)