# Cryptography
 An assortment of programs made for an undergrad cryptography course.


## AES-Sbox (sbox.py)
 The Sbox.py script is an implementation of the AES Sbox using Euclid's Extended Algorithm and matrix multiplication in GF(2^8).

 This code accepts two hexadecimal digits as input and then converts it to binary, calculates the multiplicative inverse in GF(2^8) using Euclid's Extended Algorithm, then performs matrix multiplication to return the Sbox output.

 Input must be two hexadecimal digits (i.e. FF, 4C, A9). Output will be two hexadecimal digits.


## Miller-Rabin Primality Test (prime_test.py)
 The prime_test.py code uses the Miller-Rabin Primality Test to decide if a given number is prime or composite.

 The program accepts an odd, positive integer as command line input and returns either "Composite" or "Probably Prime". The algorithm can determine primality with 99.9% accuracy.

  Requires the "Random" python module.  


## Modular Exponentiation (mod_exp.py)
 The mod_exp.py calculates x^e mod n via modular exponentiation, aka the square and multiply algorithm.

 The program accepts three arguments as input:
 \tx - the base number being raised to a power
 \te - a non-negative integer for the exponent
 \tn - a positive integer modulus
