u = input("Username>>")
p = input("Password>>")
if u == "admin" and p == "aa123456":
    print("Welcome To AA Shop")
    print("---My Product---")
    print("  1.Apple  20  THB")
    print("  2.Banana 50  THB")
    print("  3.Mango  80  THB")
    print("  4.Papaya 100 THB")
    y = int(input("Choose you Product(Type number)>>"))
    n = int(input("Piece>>"))
    if y == 1:
        print("Apple", n*20, "THB")
        print("----Thank You----")
    if y == 2:
        print("Banana", n*50, "THB")
        print("----Thank You----")
    if y == 3:
        print("Mango", n*80, "THB")
        print("----Thank You----")
    if y == 4:
        print("Papaya", n*100, "THB")
        print("----Thank You----")
    else:
        print("Wrong Number")
else:
    print("Wrong Username or Password")








