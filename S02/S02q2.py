def perfect_num(number_):
    sum=0
    for i in range(1,int(number_/2)+1):
        print(i)
        if number_%i==0:
            sum+=i            
    print(sum)
    if sum==number_:
        print('perfected')
    else:
        print('not perfected')

perfect_num(33550336)
print(6**0.5)
#perfect number formula:number=n---(2**n-1)((2**n)-1)