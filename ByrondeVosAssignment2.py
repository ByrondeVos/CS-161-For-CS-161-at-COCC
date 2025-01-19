# Print out the value of a variable in binary and decimal form.
# x must be an integer or 'float' error
x = 18
print(x,bin(x), hex(x))

# assign binary or hex values to a variable
y=0b1011
z=0xA3
print(y,z)

# add variables in any representation
w = x + y + z
print ('the sum is ', w)

# Compression

original_size = 250
dictionary_size = 50
compressed_text_size = 50

#calculate compression precentage
total_size = compressed_text_size + dictionary_size
compression = 1 - (total_size / original_size)

print('Compressed text size: ', str(compressed_text_size), 'characters')
print('     Dictionary size:', str(dictionary_size), 'characters')
print('               Total:', str(total_size), 'characters')
print('  Original text size:', str(original_size), 'characters')
print('         Compression:' , f"{compression * 100:.0f}%") #.0f formats value to 0 decimal places