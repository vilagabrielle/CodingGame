import sys
import math



message = raw_input()
N= len(message)
result=""
asc2=""

#function put each code in 7 bit
def bonformat(code):
    d=7-len(code)
    for i in range(d):
        code="0"+code
    return code



#combination of the code of each letter in one code
for t in range(N):
    asc2=asc2+bonformat(bin(ord(message[t]))[2:])


#dimension of the new message in dec
dim=len(asc2)
j=0


#creation of the unary code
while j!=dim:

    #first block: defining block of 1 or 0
    if int(asc2[j])==1:
        result=result+"0 "
    else:
        result=result+"00 "


    #count of elements by block
    compt=0
    while (compt+j<dim and int(asc2[j])==int(asc2[j+compt])) :

        compt=compt+1

    #add of the 2nd block: number of elements
    for t in range(compt):
        result=result+"0"


    j=j+compt

    if j<dim:
        result=result+" "



print result
