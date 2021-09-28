valid_input= False
while not valid_input:
    try:
        age = int(input("enter age: "))
        valid_input = True
    except ValueError:
        print("Not a number")

    if age % 2 == 1:
        print("{} is odd".format(age))
    else:
        print("{} is even".format(age))