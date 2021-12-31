def powr(x,n):
    value = x
    printVar = n
    if n == 0: #check to see if raising to 0 power
        return 1
    elif n == 1: #check to see if raising to 1 power
        return x 
    elif n>1: 
        while (n>1):
            value = value * x #multiplying x by itself n times
            n -= 1
    print "the value of", x, "to the power of",printVar,"is"
    return value
print powr(3,2) #running function
print("\n")

def prime(x,y):
    primeList = [] #creating empty list
    if (y > x): #figuring out which number is larger so know which one to start the range with
        start = x
        end = y
    else:
        start = y
        end = x
    for k in range(start, end+1): #all values between the range are true
        prime = True
        for i in range(2,k): #determining if a value in the range is prime or not by modding by i
            if (k%i==0):
                prime = False
        if prime == True: #all the values that did not have a mod of 0 are left as true and added to a list
            primeList.append(k)
    print "the prime numbers between", x , "and" , y, "are"
    return primeList
print prime(100,200) #running function
                            
                
        
