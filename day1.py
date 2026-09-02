def calculate_bill(price,quantity,discount):
    total=price*quantity
    discount_amount = total * discount /100
    final_bill = total - discount_amount
    return final_bill

result = calculate_bill(1300,2,18)

print(result)
