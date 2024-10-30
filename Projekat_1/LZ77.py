###
#   LZ77 is a lossless data compression algorithm that operates on 
#   a sliding window of input data. It achieves compression by replacing 
#   repeated occurrences of data with references to a 
#   dictionary that contains previously seen data.
#   
# example:
#   c a b v a c a d a b v a v v a v v a d 
#   window_size: 13 = lookahead_buffer + search_buffer
#   
#   search_buffer: 7     |     lookahead_buffer: 6
#   <o,l,c> = <offset, length of match, codeword>
#   <offset, how many terms are match, which term is not much>
    #     ENCODING:
    # 1)
    # [][][][][][][] | [c][a][b][v][a][c] 
    # c -> <0,0,c(c)>
    
    # 2)
    # [][][][][][][c] | [a][b][v][a][c][a]
    # a -> <0,0,c(a)>
    
    # 3)
    # [][][][][][c][a] | [b][v][a][c][a][d]
    # b -> <0,0,c(b)>
    
    # 4)
    # [][][][][c][a][b] | [v][a][c][a][d][a]
    # v -> <0,0,c(v)>
    
    # 5)
    # [][][][c][a][b][v] | [a][c][a][d][a][b]
    # a -> <3,1,c(c)>
    
    # 6)
    # [][c][a][b][v][a][c] | [a][d][a][b][v][a]
    # a -> <2,1,c(d)>
    
    # 7)
    # c [a][b][v][a][c][a][d] | [a][b][v][a][v][v]
    # a -> <7,4,c(v)>
    
    # 8)
    # c a b v a c [a][d][a][b][v][a][v] | [v][a][v][v][a][d] #lookinf into lookahead buffer because there is match
    # v -> <3,5,c(d)>
    
    # DECODING:
    # c -> <0,0,c(c)>
    # [][][][][][][c]
    
    # a -> <0,0,c(a)>
    # [][][][][][c][a]
    
    # b -> <0,0,c(b)>
    # [][][][][c][a][b]
    
    # v -> <0,0,c(v)>
    # [][][][c][a][b][v]
    
    # a -> <3,1,c(c)>
    # [c][a][b][v][a][c]
    
    # a -> <2,1,c(d)>
    # [c][a][b][v][a][c][a][d]
    
    # a -> <7,4,c(v)>
    # [c][a][b][v][a][c][a][d][a][b][v][a][v]
    
    # v -> <3,5,c(d)>
    # [c][a][b][v][a][c][a][d][a][b][v][a][v][v][a][v][v][a][d]
    
    # node - implemented!
    # tree - implemented!
    # encode
    # decode
    # write_in/out
    
###
from bitarray import bitarray


class LZ77:
    MAX_WINDOWS_SIZE = 500
    
    def __init__(self, window_size=20):
        self.window_size = min(window_size, self.MAX_WINDOWS_SIZE)
        self.lookahead_size = 15
    
    def compress(self, input_file, output_file = None):
        data = None 
        i = 0
        output_buff = bitarray(endian = 'big')
        
        try:
            with open(input_file, "rb") as input:
                data = input.read()
        except IOError:
            print("Failed to open input file!")
        
        while(i < len(data)):
            print(i)
            match = self.findLongestMatch(data,i)
            if(match):
                (mDistance, mLength) = match;
                
                output_buff.append(True)
                output_buff.frombytes(bytes([mDistance >> 4]))
                output_buff.frombytes(bytes([((mDistance & 0xf) << 4) | mLength]))
                
                print("<1, %i, %i"%(mDistance,mLength),end="")
                
                i+=mLength
            else:
                output_buff.append(False)
                output_buff.frombytes(bytes([data[i]]))
                
                print("<0,%s" % data[i],end='');
                
                i+=1;
                
        output_buff.fill()

        if(output_file):
            try:
                with open(output_file, 'wb') as output:
                    output.write(output_buff.tobytes())
                    return None 
            except IOError:
                print("Failed to write into file!")
        
        return output_buff;
    
    def decompress(self, input_file, output_file=None):
        data = bitarray(endian = 'big');
        output_buff = []
        
        try:
            with open(input_file, 'rb') as input:
                data.fromfile(input)
        except IOError:
            print('Failed to open file.')
            return
        
        while(len(data) >= 9):
            flag = data.pop(0)
            if not flag:
                byte = data[0:8].tobytes()
                
                output_buff.append(byte)
                del data[0:8]
            else:
                byte1 = ord(data[0:8].tobytes())
                byte2 = ord(data[8:16].tobytes())
                
                del data[0:16]
                dist = (byte1 << 4) | (byte2 >> 4)
                length = (byte2 & 0xf)
                
                for i in range(length):
                    print(i)
                 #   output_buff.append(output_buff[-dist])
        print('oit',output_buff)
        out_data = b''.join(output_buff)
        
        if(output_file):
            try:
                with open(output_file, 'wb') as output:
                    output.write(out_data)
                    return
            except IOError:
                print('Failed to write into file.')
        
        return out_data
    
    def findLongestMatch(self, data, current_position):
        end_of_buffer = min(current_position + self.lookahead_size, len(data)+1)
        
        mDistance = -1
        mLength = -1
        
        for j in range(current_position+2, end_of_buffer):
            start_index = max(0,current_position - self.window_size)
            sub = data[current_position:j]
            
            for i in range(start_index, current_position):
                
                rep = len(sub)//(current_position-i)
                last = len(sub) % (current_position-i)
                
                matched = data[i:current_position] * rep + data[i:i+last]
                
                if matched == sub and len(sub) > mLength:
                    mDistance = current_position-i;
                    mLength = len(sub)
                
                if(mDistance > 0 and mLength > 0):
                    return (mDistance,mLength)
                
                return None
def main():
    input_file = './inputLZ77.txt'
    output_file = './output_lz77.txt'
    
    compressor = LZ77()
 
    compressor.decompress(input_file, output_file)
  

    decompressed_data = compressor.decompress(input_file)
    print(decompressed_data)
    text = decompressed_data.decode('utf-8')
    print(text)

if __name__ == "__main__":
    main()