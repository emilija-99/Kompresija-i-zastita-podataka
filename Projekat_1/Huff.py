import os
from collections import Counter
import heapq

class Node:
    def __init__(self, symbol, freq):
        self.symbol = symbol
        self.freq = freq
        self.code = ""
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(symbols):
    pq = [Node(symbol, freq) for symbol, freq in symbols]
    heapq.heapify(pq)

    while len(pq) > 1:
        left = heapq.heappop(pq)
        right = heapq.heappop(pq)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(pq, merged)

    return pq[0] if pq else None

def generate_huffman_codes(node, prefix='', codes={}):
    if node:
        if node.symbol is not None:
            codes[node.symbol] = prefix
        generate_huffman_codes(node.left, prefix + '0', codes)
        generate_huffman_codes(node.right, prefix + '1', codes)
    return codes

def encode_content(file_path, codes):
    encoded_content = ""

    with open(file_path, 'r') as file:
        while True:
            content = file.read(1)
            if not content:
                break
            encoded_content += codes.get(content, '')

    return encoded_content

def main():
    global length
    file_path = "./file_proba.txt"
    container = Counter()

    with open('./file_proba.txt', 'r') as file:
        while True:
            content = file.read(1)
            if not content:
                break
            container[content] += 1

    symbols = [(symbol, freq / sum(container.values())) for symbol, freq in container.items()]
    huffman_tree = build_huffman_tree(symbols)
    huffman_codes = generate_huffman_codes(huffman_tree)

    print("Symbol\tFreq\tCode")
    for symbol, freq in symbols:
        print(f"{symbol}\t{freq}\t{huffman_codes.get(symbol, '')}")

    encoded_content = encode_content(file_path, huffman_codes)

    encoded_file_path = "./encoded_file.txt"
    with open('./encoded_file_huff', "w") as encoded_file:
        encoded_file.write(encoded_content)

if __name__ == "__main__":
    main()
