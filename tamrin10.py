n = int(input("lotfan yek adad az 2 ta 1000 vared konid:\n"))

while n < 2 or n > 1000 :
    print("meghdar vared shode dar bazeye sahih nemibashad!")
    n = int(input("lotfan mojaddad yek adad az 2 ta 1000 vared konid:\n"))

while n != 1 :
    if n%2 == 0:
        n = n/2
        print(int(n))
    else:
            n = 3*n + 1
            print(int(n))