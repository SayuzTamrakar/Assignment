a = input (" Enter any word : ")

if len(a) > 1:
    swap = a[-1] + a [1:-1] + a [0]


else:
    swap = a
print (" The Original Word : ", a)
print ( " The Swapped Word: " , swap)