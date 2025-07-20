def calculate_discount(price, discount_percentage):
    # Write code here
    fprice = round(price - price * discount_percentage/100, 2)
    return(fprice)

print(calculate_discount(75.5,10))