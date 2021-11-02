def vat(total):
    result = total+(total*7/100)
    return (result)
print(vat(int(input("Price :"))))