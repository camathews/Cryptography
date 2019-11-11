import random

# main function, performs the primality test.
def main(n):
    q = n-1
    k = 0
    while 1 == (q%2):
        k+=1
        q = q/2
    a = random.randint(1, n-1)
    if(mod_exp(a, q, n) == 1):
        return False
    e = q
    for j in range(0,k):
        if((n - 1) == (mod_exp(a, e, n))):
            return False
        e = 2 * e
    return True


# function for Modular Exponentiation.
def mod_exp(x, e, n):
    e_bits = bin(e)[2:] # convert int e into binary, also trim off "0b" from byte string.
    y = 1
    for i in range(len(e_bits)): # incrementing for loop within the length of e_bit.
        y = y**2 % n
        if(e_bits[i] == '1'): # if a digit in e_bits is a 1.
            y = x*y % n
    return y


# function for taking and filtering usr input.
def input_func():
    test = 0
    error = "n must be an odd, positve integer.\n"
    print("\tMiller-Rabin Primality Test\n")
    while test == 0:
        n = input("Enter an odd, positive integer to test the primality of (n): ")
        # try: convert n to int, if error: take input again, if no error: check that n is positve and odd.
        try:
            n = int(n)
        except:
            print(error)
            test = 0
        else:
            if(n%2 == 0):
                print(error)
                test = 0
            elif(n <= 0):
                print(error)
                test = 0
            else:
                test = 1
                return n

n = input_func()
booleArray = []
# performs the test 5 times and adds the result to an array.
# If the test returns composite (True) at least once, n is considered composite.
# If the test returns prime (False) 5 times, n is considered probably prime with 99.9% accuracy.
for i in range(0,5):
    booleArray.append(main(n))
if(True in booleArray):
    print(n, "is composite.")
else:
    print(n, "is probably prime.")
