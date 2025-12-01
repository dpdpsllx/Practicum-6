w = input()
letter = w[0]      
number = int(w[1]) 
col = ord(letter) - ord('a') + 1  
if (col + number) % 2 == 0:
    print("черный")
else:
    print("белый")
