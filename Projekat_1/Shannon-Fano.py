import os
from collections import Counter

length = 0;
container = {}

class Node:
    def __init__(self, symbol, freq) -> None:
        self.symbol = symbol
        self.freq = freq 
        self.code = ""

def split(symbols):
    total_freq = sum(symbol.freq for symbol in symbols)
    current_freq = 0
    split_index = -1

    for i,sybmol in enumerate(symbols):
        current_freq +=sybmol.freq
        if current_freq >= total_freq / 2:
            split_index = i
            break
    return symbols[:split_index+1], symbols[split_index+1:]

def shanno_tree(symbols):
    if len(symbols)<=1:
        return
    symbols_left, symbols_right = split(symbols)

    for symbol in symbols_left:
        symbol.code += "0"

    for symbol in symbols_right:
        symbol.code += "1"

    shanno_tree(symbols_left)
    shanno_tree(symbols_right)

def encode_content(file_path, symbols):
    encoded_content = ""

    with open(file_path, 'r') as file:
        while True:
            content = file.read(1)
            if not content:
                break
            for symbol in symbols:
                if symbol.symbol == content:
                    encoded_content += symbol.code
                    break

    return encoded_content
def main():
    global length
    file_path = os.path.join("./file_proba.txt")
    with open(file_path, 'r') as file:
        while True:
            content = file.read(1)
            if not content:
                break
            container[content] = container.get(content,0)+1
            length+=1
    sorted_ = sorted(container.items(), key = lambda x: x[1], reverse=True)
    print(length)
    symbols = [Node(symbol, freq / length) for symbol, freq in sorted_]
    shanno_tree(symbols)

    print("Symbol\tFreq\tCode")
    for symbol in symbols:
        print(f"{symbol.symbol}\t{symbol.freq}\t{symbol.code}")

    encoded_content = encode_content(file_path, symbols)

    encoded_file_path = os.path.join("./encoded_file.txt")
    with open(encoded_file_path, "w") as encoded_file:
        encoded_file.write(encoded_content)
if __name__ == "__main__":
    main()


def sort(characters):
    value_frequency = Counter(characters.values())
    sorted_keys = sorted(characters, key=lambda x: value_frequency[characters[x]],reverse=False)
    sorted_dict = {key: characters[key] for key in sorted_keys}
    
    return sorted_dict

def freq(characters):
    total_length = sum(characters.values())  # Assuming you want to divide each value by the total length of the dictionary
    for key in characters:
        characters[key] /= total_length  # Update the value in the dictionary
    return characters




# container = sort(container)
# container = freq(container)

