# Function - Number Sorter
def NumberSorter(numlist, length, sortby):
    n = 0
    if sortby in ("A", "a"):
        # sorts from lowest to highest
        sortedlist = sorted(numlist)
        print("In Ascending Order: ")
        for i in range(length):
            print(sortedlist[n])
            n += 1
        #print("In Ascending Order: ", sortedlist)
    elif sortby in ("D", "d"):
        # sorts from highest to lowest
        sortedlist = sorted(numlist, reverse=True)
        print("In Descending Order: ")
        for i in range(length):
            print(sortedlist[n])
            n += 1
        #print("In Descending Order: ", sortedlist)
    else:
        raise ValueError

numlist = []
length = int(input("Length of numbers to sort: "))
print("Enter numbers: ")

for i in range(length):
    num = int(input(""))
    numlist.append(num)

print("A - Ascending")
print("D - Descending")
sortby = input("Sort in: ")

NumberSorter(numlist, length, sortby)
