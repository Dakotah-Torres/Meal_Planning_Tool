import openfoodfacts
import json


class HomeStock:
        
    def __init__(self):
        self.fields = [
            "code",                    # barcode — your SKU lookup key
            "product_name",            # -> name
            "brands",                  # optional, useful for disambiguation in UI
            "quantity",                # raw quantity string as printed on package
            "product_quantity",        # normalized quantity
            "product_quantity_unit",   # normalized unit (g/ml)
            "serving_size",            # raw serving size string
            "serving_quantity",        # normalized serving size -> your serving_size
            "serving_quantity_unit",   # -> your serving_unit
            "nutrition_data_per",      # "serving" or "100g" — tells you which nutriments to trust
            "nutriments.energy-kcal_serving",
            "nutriments.energy-kcal_100g",
            "nutriments.proteins_serving",
            "nutriments.proteins_100g",
            "nutriments.carbohydrates_serving",
            "nutriments.carbohydrates_100g",
            "nutriments.fat_serving",
            "nutriments.fat_100g",
            "nutriments.fiber_serving",
            "nutriments.fiber_100g",
            "nutriments.sugars_serving",
            "nutriments.sugars_100g",
            "nutriments.sodium_serving",
            "nutriments.sodium_100g",
        ] 
    
    
    def look_up_sku(self, sku):
        my_agent = "HomeStockApp/1.0 (dtorres@dtdevtech.com)"
        api = openfoodfacts.API(user_agent=my_agent)
        
        
        product = api.product.get(sku, fields=self.fields)
        if product is None:
            return ValueError(f"No product found for SKU: {sku}")
        
        return product
        


