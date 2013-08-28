# This is where the answers to Chapter 9 questions for the BSS Dev RampUp go
# Name:Mike Lattanzio

#9.1 - My Attempt


fin = open ('words.txt') 
for line in fin:
	word = line.strip()
	for word.len(3)
	print word
	else
	print
	"No Cigar!"


	
#9.2 - My Attempt
def has_no_e (word):
	if word.strip()
	return "True"
	else 
	return "False"

has_no_e (rock)

#Solution:

def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
return True


#9.3 - My Attempt

forbidden letters = (l, m, n, o, p)

def avoid_it (word, string):
	word.strip()
	string.strip()
	
	if forbidden letters
	return False

	else 
	return True

avoid_it ("clown")

#Solution: 

def avoids(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
return True


#9.4 - My Attempt

forbidden letters = (b, d, f, h, a)
def uses_only (word, string):
	word.strip()
	if word.strip(forbidden letters)
	return True

#Solution:

def uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
return True









