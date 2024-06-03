'''
Move the first letter of each word to the end of it, 
then add "ay" to the end of the word. 
Leave punctuation marks untouched.

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
'''
text='Pig latin is cool'

def pig_it(text):
    splitText = text.split(' ')
    igpay = []
    for word in splitText:
        word = word+word[0]+'ay'
        word = word[1:]
        
        igpay.append(word)
    return(' '.join(igpay))

phrase = pig_it(text)
print (phrase)