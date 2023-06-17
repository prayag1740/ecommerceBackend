from decimal import Decimal
from bson.decimal128 import Decimal128

class ProductController:

    def search_and_filter_products(self, query_params, prod_qset):
        keyword = query_params.get('keyword')
        if keyword:
            prod_qset = prod_qset.filter(name__icontains=keyword)
        
        to_remove_columns = ['keyword' , 'page' , 'limit']
        for key in to_remove_columns:
            query_params.pop(key, None)

        if query_params:
            prod_qset = prod_qset.filter(**query_params.dict())

        return prod_qset
    

