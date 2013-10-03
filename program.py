def divisors(n):
    list_of_divisors = []
    if n >= 2:
        for i in range(1, n / 2 + 1):
            if (n % i == 0):
                list_of_divisors.append(i)
    list_of_divisors.append(n)
    return list_of_divisors

def askUserForNumber():
     return raw_input("Type the number you want to see the divisors of: ")

def isPrime(n):
    if len(divisors(n)) == 2:
        return True
    return False

if __name__ == '__main__':
    # get input from the user
    while (True):
        num = askUserForNumber()

        while not (num.isdigit()):
            num = askUserForNumber()

        print divisors(int(num))
        if (isPrime(int(num))):
            print "The number is prime!"
