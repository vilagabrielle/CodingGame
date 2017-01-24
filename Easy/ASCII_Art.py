import sys
import math


#function that give the position of a big or small letter in the alphabet
def compt(letter):
    alpha1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    alpha2=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    compt=1

    if letter in alpha1:
        alpha=alpha1
        return alpha.index(letter)+1

    if letter in alpha2:
        alpha=alpha2
        return alpha.index(letter)+1
    else:
        return 27

#width of each letter
l = int(raw_input())
#height of each letter
h = int(raw_input())
#line of text that is going to be treated
t = raw_input()

ts= [ i for i in t]
tsn=len(ts)



for i in xrange(h):
#the drawing will be done line by line

    result= ""

    #string of characters ABCDEFGHIJKLMNOPQRSTUVWXYZ? represented in ASCII Art
    row = raw_input()

    #combination of letter stock in "result"
    for s in range(tsn):

        debut=l*(compt(ts[s])-1)
        fin=l*compt(ts[s])

        result=result+row[debut:fin]


    print result
