# Square and Multiply (Modular Exponentiation)
# x^e mod n

def main():
    print("Square and Multiply (Modular Exponentiation)")
    print("Calculates x^e mod n")

    # vars declared via user input.
    x = int(input("Enter an integer for x: "))
    e = int(input("Enter a non-negative integer for e: "))
    n = int(input("Enter a positive integer modulus for n: "))

    e_bits = bin(e)[2:] # convert int e into binary, also trim off "0b" from byte string.

    y = 1
    for i in range(len(e_bits)): # incrementing for loop within the length of e_bit.
        y = y**2 % n
        if(e_bits[i] == '1'): # if a digit in e_bits is a 1.
            y = x*y % n

    print("x^e mod n = ", y)

main() # calls the main function defined above.
