def my_function():
    price1 = int(input("item1: "))
    price2 = int(input("item2: "))
    a_dict = { "item1" : int(price1), "item2" : int(price2) }
    list1 = list(a_dict.values())
    sum1 = 0
    for i in list1:
        sum1 += i
        totaltax = sum1 * 0.24
        print(sum1)
        print(totaltax)


my_function()