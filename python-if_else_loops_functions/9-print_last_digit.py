#!/usr/bin/python3
"""String-i böyük hərflərlə çap edən funksiya"""

def uppercase(str):
    """
    Bir string-i böyük hərflərlə çap edir, ardınca yeni sətir əlavə edir.
    """
    for char in str:
        ascii_val = ord(char)
        # Kiçik hərflərin ASCII diapazonu (97-122)
        if ascii_val >= 97 and ascii_val <= 122:
            # Böyük hərfə çevirmək üçün 32 çıxılır
            char_to_print = chr(ascii_val - 32)
        else:
            char_to_print = char
        
        # Birinci print funksiyası (simvollar üçün)
        print("{}".format(char_to_print), end="")
    
    # İkinci print funksiyası (yeni sətir üçün)
    print("{}".format(""))
