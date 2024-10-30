class bitio:
    def __init__(self, file):
        self.file = file
        self.byte_buffer = 0
        self.bits_in_buffer = 0

    def write_bits(self, value, num_bits):
        """
        Writes a specified number of bits from an integer to the output stream.

        Parameters:
        - value: Integer value to write.
        - num_bits: Number of bits to write from the integer value.
        """
        # Write bits one by one
        for i in range(num_bits):
            bit = (value >> (num_bits - 1 - i)) & 1
            self.byte_buffer = (self.byte_buffer << 1) | bit
            self.bits_in_buffer += 1

            # If buffer is full (8 bits), write it to file
            if self.bits_in_buffer == 8:
                self.file.write(bytes([self.byte_buffer]))
                self.byte_buffer = 0
                self.bits_in_buffer = 0

    
    def read_bit(self, num_bits):
        """
        Reads a specified number of bits from the input stream.

        Parameters:
        - num_bits: Number of bits to read from the input stream.

        Returns:
        - Integer value containing the bits read from the input stream.
        """
        result = 0

        # Read bits one by one
        for i in range(num_bits):
            # If buffer is empty, refill it
            if self.bits_in_buffer == 0:
                self.byte_buffer = ord(self.file.read(1)) if isinstance(self.file, file) else self.file.read(1)
                self.bits_in_buffer = 8

            # Extract bit from buffer
            bit = (self.byte_buffer >> (self.bits_in_buffer - 1)) & 1
            result = (result << 1) | bit
            self.bits_in_buffer -= 1

        return result

    def flush(self):
        """
        Flushes any remaining bits in the buffer to the output stream.
        """
        if self.bits_in_buffer > 0:
            self.file.write(bytes([self.byte_buffer]))

    def close(self):
        """
        Closes the BitIO instance and flushes any remaining bits.
        """
        self.flush()
        self.file.close()
