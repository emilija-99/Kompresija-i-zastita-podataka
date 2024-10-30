def is_uniquely_decodable(coded):
    M0 = set(coded)
    M1 = set()
    M2 = set()
    
    while(True):
        for code in M0:
            if any(code.startswith(prefix) for prefix in M1):
                M1.add(code)
            if any(code.endswith(suffix) for suffix in M2):
                M2.add(code)
        
        if not M1 or not M2:
            return True
        elif M2 and M1:
            return False
        
        M0 = M0 - M1 - M2 
        
        M1.clear()
        M2.clear()
        
code_strings = {'a', 'ab', 'ac', 'b', 'bc', 'c'}


uniquely_decodable = is_uniquely_decodable(code_strings)

if uniquely_decodable:
    print("The code is uniquely decodable.")
else:
    print("The code is not uniquely decodable.")