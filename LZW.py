def encode(text):
    dict_size = 256
    dictionary = {chr(i): i for i in range(dict_size)} 
    
    foundChar = ""
    encoded_list = []
    
    for character in text:
        char_add = foundChar + character
        if char_add in dictionary:
            foundChar = char_add
        else:
            encoded_list.append(dictionary[foundChar])
            dictionary[char_add] = dict_size
          
            dict_size += 1
            foundChar = character

    if foundChar:
        encoded_list.append(dictionary[foundChar])
        
    return encoded_list


def decode(encoded_list):
    dict_size = 256
    dictionary = {i: chr(i) for i in range(dict_size)}  
    
    first_code = encoded_list.pop(0)
    characters = dictionary[first_code]
    
    decoded_result = [characters]
    
    for code in encoded_list:
        if code in dictionary:
            entry = dictionary[code]
        else:
            entry = characters + characters[0]
        
        decoded_result.append(entry)
        
        dictionary[dict_size] = characters + entry[0]
        dict_size += 1
        
        characters = entry
    
    return ''.join(decoded_result)


compress = encode('geekific-geekific')
print("Encoded:", compress)

decompress = decode(compress)
print("Decoded:", decompress)

# https://www.youtube.com/watch?v=1KzUikIae6k