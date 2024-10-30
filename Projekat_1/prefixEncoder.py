import ast
class prefixEncoder:
    def __init__(self):
        self.codes = {}
    
    def build_encoding(self, symbol_freq):
        # symbols are sorted based on their frequencies in descending order
        # symbols with higher frequencies are assigned shorter codes, which helps in achieving compression
        sorted_symbols = sorted(symbol_freq.items(), key = lambda x : x[1], reverse=True)
        current_code = ' 0'
        
        for symbol, _ in sorted_symbols:
            self.codes[symbol] = current_code;
            current_code = self._increment_code(current_code)
###
#   build_encoding
#{'K': '0'}
#{'K': '0', 'M': '1'}
#{'K': '0', 'M': '1', 'S': '10'}
#{'K': '0', 'M': '1', 'S': '10', 'A': '11'}
#{'K': '0', 'M': '1', 'S': '10', 'A': '11', 'B': '100'}
#{'K': '0', 'M': '1', 'S': '10', 'A': '11', 'B': '100', 'C': '101'}
#{'K': '0', 'M': '1', 'S': '10', 'A': '11', 'B': '100', 'C': '101', 'D': '110'}
###    
    
    def encode(self, text):
        encoded_text = ''
        for symbol in text:
            for key, code in self.codes.items():
                if(symbol == key):
                    encoded_text+=code;
                    break
            
        return encoded_text

    def decode(self, encoded_text):
        decoded_text = ''
        decoded_symbols = []
        for char in encoded_text.split():
            for symbol,code in self.codes.items():
                code_str = str(code).replace(' ','')
                current_code_str = str(char)
                if(code_str.__eq__(current_code_str)):
                    decoded_symbols.append(symbol)
        
        decoded_text = ''.join(decoded_symbols)
        return decoded_text
                      
    
    def _increment_code(self, code):
        if not code:
            return ' 1'
        else:
            incremented_int = int(code.replace(' ', ''), 2) + 1
            incremented_bin = format(incremented_int, 'b')
            if incremented_bin.startswith('0'):
                return ' ' + incremented_bin
            else:
                return ' ' + incremented_bin

encoder = prefixEncoder()

symbol_freq = {'A':5, 'B':3, 'C':2, 'D':1, 'S':15, 'K':43, 'M':23}
encoder.build_encoding(symbol_freq)

text = 'KBABACDSK'

encoded_text = encoder.encode(text)
print("encoded_text: ",encoded_text)

decoded_text = encoder.decode(encoded_text)
print("decoded_text: ", decoded_text)

if(text.__eq__(decoded_text)):
    print("Successfully decoded text!")
