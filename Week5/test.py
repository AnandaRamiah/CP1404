list2 = ['black', 'blue', 'green', 'orange', 'purple', 'red', 'silver', 'white']

list1 = ['aye', 'bee', 'sea']


def size_compare(list1, list2):
    if len(list1) == len(list2):

        return 0

    elif len(list1) > len(list2):

        return 1

    else:

        return -1

lol=size_compare(list1,list2)
print(lol)
