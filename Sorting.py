
#bubble sorting
def sorting(array) :
    n=len(array)
    while (n>1) :
        for i in range(n-1) :
            if (array[i]>array[i+1]) :
                temp= array[i]
                array[i] = array[i+1]
                array[i+1] = temp
        n-=1

#filling array
def fillArray(array) :
    num = input("Enter how many elements you want:")
    print ('Enter numbers in array: ')
    for i in range(int(num)):
        n = input("num :")
        array.append(int(n))



array = list()
fillArray(array)
print ('ARRAY: ',array)
sorting(array)
print ('SORTED ARRAY: ',array)
    