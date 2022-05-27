def q1():
    amounts=[1000, 2200, 800, 360]
    rate = 0.05
    def balance_after_years(balance, rate):
        years = int(input("How many years balance stay in account? "))
        for year in range(years):
            balance+=balance*rate
        return balance
    new_amounts = list()
    for x in amounts:
        new_amounts.append(balance_after_years(x, rate))
    print(new_amounts)
    """
        amounts[0]:
        1st year: 1000 + 1000*0.05
        2nd year: 1000 + 2*1000*0.05 + 1000*(0.05)^2
        3rd year: 1000 + 3*1000*0.05 + 2*1000*(0.05)^2 + 1000*(0.05)^3
        nth year: 1000 + n*1000*0.05 + (n-1)*1000*(0.05)^2 + .... + 2*1000*(0.05)^(n-1) + 1000*(0.05)^n
        amounts[1]:
        nth year: 2200 + n*2200*0.05 + (n-1)*2200*(0.05)^2 + .... + 2*2200*(0.05)^(n-1) + 2200*(0.05)^n
        amounts[2]:
        nth year: 800 + n*800*0.05 + (n-1)*800*(0.05)^2 + .... + 2*800*(0.05)^(n-1)  + 800*(0.05)^n
        amounts[3]:
        nth year: 360 + n*360*0.05 + (n-1)*360*(0.05)^2 + .... + 2*360*(0.05)^(n-1)  + 360*(0.05)^n
    """
#q1()
def q2():
    def recursion_factorial(n):								
       if n == 0:								
           print(n,"!=1")								
           return 1								
       else:								
            print(n,"!=",n,"*",n-1,"!")								
            return n*recursion_factorial(n-1)						        								
    result=0								
    result=recursion_factorial(4)								
    print("\nresult =",result)
    """
        1) Imagine that n is an integer larger than 0 and 2:
            1: n != 0, recursion_factorial(n) returns n*recursion_factorial(n-1)
            2: n - 1 != 0, recursion_factorial(n) returns n*(n-1)*recursion_factorial(n-1)
            3: n - 2 != 0, recursion_factorial(n) returns n*(n-1)*(n-2)*recursion_factorial(n-2)
            .
            .
            .
            n: n - n == 0, recursion_factorial(n) returns n*(n-1)*(n-2)*...*recursion_factorial(n-n) = n*(n-1)*(n-2)*...*1 = n!

            if I do not use the stop condition in the above program, this program just prints (n,"!=",n,"*",n-1,"!"),
            then stops, there will be no recursion.
    """
#q2()
def q3():
    def TowerOfHanoi(n , source, destination, auxiliary): 
        if n==1: 
            print ("Move disk 1 from source",source,"to destination",destination) 
            return
        TowerOfHanoi(n-1, source, auxiliary, destination) 
        print ("Move disk",n,"from source",source,"to destination",destination) 
        TowerOfHanoi(n-1, auxiliary, destination, source) 
              
    n = 4
    TowerOfHanoi(n,'B','C','A')
#q3()
def q4():
    def fibonacci(order):
        if(order != 1) and (order != 2):
            return fibonacci(order-1)+fibonacci(order-2)
        else:
            return 1
        return 0
    for x in range(1,14):
        print(fibonacci(x))
q4()
