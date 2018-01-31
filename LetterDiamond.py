
def LetterDiamond( letter ):
    # Prints a diamond starting with letter 'A'
    #   and hits its peak at the letter provided
    
    # Break if not a string
    try:
        letter = letter.upper()
    except AttributeError:
        print( 'Letter not provided')
        return
    
    # "Break" if the letter is A
    if (letter == 'A'):
        print( 'A' )

    # Break if more than one letter or not a letter
    try:
        N = ord(letter) - 65
    except TypeError:
        print('Letter not provided')
        return
    
    # Break if not a letter
    if ( ord(letter) <= 64 | ord(letter) >= 91 ):
        print( 'Letter not provided' )
        return
    
    # First Section
    for i in range(N):
        if ( i == 0 ):
            print(" "*N + chr( 65 + i))
        else:
            print( " "*(N - i) +  chr(65 + i) + 
                  " "*((i-1)*2+1) + chr(65 + i) )
        
    # Peak
    print(letter + (2*(N-1)+1)*" " + letter)
    
    # Last Section
    for j in range(N):
        k = N - 1 - j
        if ( k == 0 ):
            print(" "*N + chr( 65 + k) )
        else:
            print( " "*(N-k) + chr(65+k) + 
                  " "*((k-1)*2+1) + chr(65+k) )
    return

LetterDiamond('C')
LetterDiamond('j')
LetterDiamond(6)
LetterDiamond('"')
LetterDiamond('db')
# LetterDiamond()