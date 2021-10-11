numbers = [3, 1, 4, 1, 5, 9, 2]
locator = 9

numbers[0] = 10
numbers[6] = 1
for i in range(2, 7):
    print(numbers[i])
if locator in numbers:
    print("present")
else:
    print("absent")
