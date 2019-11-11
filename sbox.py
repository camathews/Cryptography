#AES S-BOX part 2
#ax = dividend
#bx = divisor
#q = quotient -> q is represented as a decimal number that is added to every iteration.
def divide(ax, bx, q, qList):
    axCount = count_shift(ax)
    bxCount = count_shift(bx)
    shiftAmount = bxCount - axCount
    q = find_quotient(q, shiftAmount)
    subtractor = shift(bx, shiftAmount)
    remainder = int(ax,2) ^ int(subtractor,2)
    if(remainder == 0):
        qList.append(bin(q)[2:].zfill(9))
        return 
    if(int(bx, 2) > remainder):
        remainder = bin(remainder)[2:].zfill(9)
        qList.append(bin(q)[2:].zfill(9))
        q = 0
        divide(bx, remainder, q, qList)
    else:
        remainder = bin(remainder)[2:].zfill(9)
        divide(remainder, bx, q, qList)
    
#countShift counts the 0's before the first 1.
def count_shift(bitStr):
    for i in range(0, len(bitStr)):
        if(bitStr[i] == '1'):
            return i

#performs a bit shift
def shift(bitStr, count):
    for i in range(0, count):
        bitStr = bitStr + '0'
    bitStr = bitStr[count:]
    return bitStr

#adds the appropriate amount to the quotient
def find_quotient(q, count):
    if(count == 0):
        q = q + 1
    elif(count == 1):
        q = q + 2
    else:
        q = q + (2**count)
    return q

#calculates the multiplicative inverse
def calc_inverse(qList):
    w0 = "000000000"
    w1 = "000000001"
    for i in qList:
        store = []
        for j in range(0, len(w1)):
            if(w1[j] == '1'):
                store.append(int(i,2) << (8-j))
        total = 0
        for k in store:
            total = total ^ k
        total = total ^ int(w0, 2)              
        w0 = w1
        w1 = bin(total)[2:].zfill(9)
    return w0
            
def matrix_calc(inv):
    start = "10001111"
    constant = "01100011"
    product = ""
    for i in range(0, 8):
        xyz = ""
        shift = start[8-i:]
        new = shift + start[:8-i]
        for j in range(0, len(start)):
            xyz = xyz + str((int(new[j], 2) & int(inv[7-j], 2)))
        xorTotal = 0
        for k in xyz:
            xorTotal = xorTotal ^ int(k,2)
        product = str(xorTotal) + product
    return bin(int(product, 2) ^ int(constant, 2))[2:].zfill(8)


def main():
    divisor = str(input("Enter hex value: "))
    divisor = bin(int(divisor, 16))[2:].zfill(9)
    dividend = "100011011"
    quotient = 0
    qList = []
    
    divide(dividend, divisor, quotient, qList)
    inv = calc_inverse(qList)
    temp = hex(int(inv, 2))
    print("Multiplicative Inverse: " + temp[2:].upper() + " (base16)")
    matrix = matrix_calc(inv[1:])
    temp = hex(int(matrix, 2))
    print("S-Box Calculation: " + temp[2:].upper() + " (base16)")
main()

