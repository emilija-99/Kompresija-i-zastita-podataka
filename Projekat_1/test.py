import struct
import sys
import math

def LZ77_search(search, look_ahead):
    ls = len(search)
    llh = len(look_ahead)
 
    if ls == 0:
        return (0, 0, look_ahead[0])
	 
    if llh == 0:
        return (-1, -1, "")
    
    best_length = 0
    best_offset = 0 
    buf = search + look_ahead

    search_pointer = ls	
    
    for i in range(0, ls):
        length = 0
        while buf[i + length] == buf[search_pointer + length]:
            length += 1
            if search_pointer + length == len(buf):
                length -= 1
                break
            if i + length >= search_pointer:
                break	 
        if length > best_length:
            best_offset = i
            best_length = length

    return (best_offset, best_length, buf[search_pointer + best_length])

def decoder(name, out, MAX_SEARCH):
    with open(name, "rb") as file:
        input_data = file.read()
    
    chararray = bytearray()
    i = 0

    while i < len(input_data):
        offset_and_length, char = struct.unpack(">Hc", input_data[i:i + 3])
        offset = offset_and_length >> 6
        length = offset_and_length - (offset << 6)
        i = i + 3

        if offset == 0 and length == 0:
            chararray.append(char[0])
            out.write(chararray)
            chararray = bytearray()  # Reset chararray for next sequence
        else:
            
            start_index = len(chararray) - MAX_SEARCH + offset - 1
            print(start_index)
            for _ in range(length):
                chararray.append(chararray[start_index])
                start_index += 1
            chararray.append(char[0])  # Append the first byte of char (which is bytes) to bytearray
            out.write(chararray)
            chararray = bytearray()  # Reset chararray for next sequence

def main():
    x = 4
    MAXSEARCH = 1
    MAXLH = int(math.pow(2, (x - (math.log(MAXSEARCH, 2)))))

    file_to_read = 'inputLZ77.txt'
    with open("output_LZ77.txt", "wb") as file:
        input_data = parse(file_to_read)
        searchiterator = 0
        lhiterator = 0

        while lhiterator < len(input_data):
            search = input_data[searchiterator:lhiterator]
            look_ahead = input_data[lhiterator:lhiterator + MAXLH]
            offset, length, char = LZ77_search(search, look_ahead)

            shifted_offset = offset << 6
            offset_and_length = shifted_offset + length 
            ol_bytes = struct.pack(">Hc", offset_and_length, bytes([char]))
            file.write(ol_bytes) 

            lhiterator = lhiterator + length + 1
            searchiterator = lhiterator - MAXSEARCH

            if searchiterator < 0:
                searchiterator = 0

    with open("output_LZ77.txt", "rb") as compressed_file:
        with open("decoded_output.txt", "wb") as decoded_file:
            decoder("output_LZ77.txt", decoded_file, MAXSEARCH)

def parse(file):
    with open(file, "rb") as f:
        return f.read()

if __name__ == "__main__":
    main()
