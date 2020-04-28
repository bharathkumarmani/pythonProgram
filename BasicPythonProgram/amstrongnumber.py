def to_find_amstrong_number(number):
    for i in range(number):
        num = i
        result = 0 
        n = len(str(i))
        while (i!=0):
            digit = i%10
            result = result + digit **n
            i = i//10
        if num == result:
            print(num)
             
print(to_find_amstrong_number(1001))