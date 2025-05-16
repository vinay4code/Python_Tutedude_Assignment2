#Sum of integers from 1 to 50
def sum(a,b):
    sum = 0
    for i in range(a,b+1):
        sum += i
    return sum

print(f" The sum of integers from 1 to 50 is: {sum(1,50)}")