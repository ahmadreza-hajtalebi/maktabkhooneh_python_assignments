n = int(input("lotfan yek adad sahih vared konid:\n"))

if n % 3 == 0 and n % 5 == 0:
    print("افسانه ای")
elif n % 3 == 0:
    print("جادویی")
elif n % 5 == 0:
    print("نفرین شده")
else:
    print("معمولی")