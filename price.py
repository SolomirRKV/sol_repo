def format_price(price):
    price = int(float(price))
    return f'Цена {price} руб'

display_price = format_price('56.24')
print (display_price)