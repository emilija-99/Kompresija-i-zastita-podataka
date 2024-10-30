window_size = 20
lookahead_buffer_size = 15
search_buffer_size = window_size - lookahead_buffer_size

class Trouple:
    def __init__(self, offset, length, indicator):
        self.offset = offset
        self.length = length
        self.indicator = indicator

    def __repr__(self):
        return f"Trouple(offset={self.offset}, length={self.length}, indicator='{self.indicator}')"

def match_length_from_index(text, window, text_index, window_index):
    if text_index >= len(text) or text[text_index] != window[window_index]:
        return 0
    else:
        return 1 + match_length_from_index(text, window + text[text_index], text_index + 1, window_index + 1)

def find_encoding_token(text, search_buff):
    if not text:
        return Trouple(-1, -1, "")
    
    length, offset = 0, 0
    
    if not search_buff:
        return Trouple(offset, length, text[0])
    
    for i, character in enumerate(search_buff):
        found_offset = len(search_buff) - i
        if character == text[0]:
            found_length = match_length_from_index(text, search_buff, 0, i)
            if found_length >= length:
                offset, length = found_offset, found_length
    return Trouple(offset, length, text[length] if length < len(text) else '')

def LZ77compress(text):
    output = []
    search_buff = ""
    
    while text:
        token = find_encoding_token(text, search_buff)
        
        search_buff += text[: token.length + 1]
        if len(search_buff) > search_buffer_size:
            search_buff = search_buff[-search_buffer_size:]
        
        text = text[token.length + 1:]
        
        output.append(token)
    return output

def LZ77decompress(tokens):
    output = ""
    for token in tokens:
        if token.offset > 0:
            for _ in range(token.length):
                output += output[-token.offset]
        
        output += token.indicator
    return output

TEXT = "cabracadabrarrarrad"
compressed = LZ77compress(TEXT)
print("Compressed:", compressed)

decompressed = LZ77decompress(compressed)
print("Decompressed:", decompressed)
