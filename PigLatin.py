'''
Move the first letter of each word to the end of it, 
then add "ay" to the end of the word. 
Leave punctuation marks untouched.

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
'''
text='Pig latin is cool'
splitText = text.split(' ')
print(splitText)

def pig_it(text):
    splitText = text.split(' ')
    print(splitText[0][0])

pig_it(text)