def binary_search(number,numbers):
    low=0
    high=len(numbers)-1
    while high>=low:
        midpoint=(low+high)//2
        if numbers[midpoint]==number:
            print('number found')
            break
        elif numbers[midpoint]>number:
            high=midpoint-1  
        else:
            low=midpoint+1
    else:
        print('number not found')
binary_search(500,[1,2,3,4,5,6,7,8,9,10])