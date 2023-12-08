symbol = input()
ascii_code = ord(symbol)
binary_representation = format(ascii_code, "b")
count_of_ones = binary_representation.count("1")
parity_bit = '0'
if count_of_ones % 2 == 1:
    parity_bit = '1'
ans = parity_bit + binary_representation
print(ans)
