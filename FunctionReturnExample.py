def vat(total):
    result = total+(total*7/100)
    return (result)
print("Price Total =",(vat(int(input("Price :")))))