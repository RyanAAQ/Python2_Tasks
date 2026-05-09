def discount(name, price, promo_code):

    if promo_code.lower() == "save10":
        discount_price = price * (10 / 100)
        final_price = price - discount_price
        
        return final_price
        
    elif promo_code.lower() == "halfoff":
        discount_price = price * (50 / 100)
        final_price = price - discount_price
        
        return final_price
        
    else:
        final_price = price
        
        return final_price
