# returns a list of divisors of n
def divisors(n):
    list_of_divisors = []
    if n >= 2:
        for i in range(1, n / 2 + 1):
            if (n % i == 0):
                list_of_divisors.append(i)
    list_of_divisors.append(n)
    return list_of_divisors

# function to ask a user for a number
def askUserForNumber():
    num = raw_input("Type a number: ")
    #check if user entered a number
    while not (num.isdigit()):
        num = raw_input("That is not a number. \nType a number: ")
    return num

# return True/False if the number is prime
def isPrime(n):
    if len(divisors(n)) == 2:
        return True
    return False

if __name__ == '__main__':
    #make a continuous loop
    while (True):
        num = askUserForNumber()

        print divisors(int(num))
        #print sentence only if number is prime
        if (isPrime(int(num))):
            print "The number is prime!"
