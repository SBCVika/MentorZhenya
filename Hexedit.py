# DRAFT

filename = "eeprom_CL2400_BASE.bin"
block_size = 32
def display_binary(filename):
    file = open(filename, 'rb')
    block_number=1
    while True:
        block = file.read(block_size)  # Adjust the buffer size as needed
        if not block:
            break
        block_number = block_number+1
        print("0x"'{:03x}'.format(block_size*block_number), end = " ") # address representation
        print('-'.join('{:02x}'.format(byte) for byte in block), end = '\n')
    file.close()
display_binary("eeprom_CL2400_BASE.bin")