'''
Move the first letter of each word to the end of it, 
then add "ay" to the end of the word. 
Leave punctuation marks untouched.

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
'''
text='Quis custodiet ipsos custodes ?'

def pig_it(text):
    splitText = text.split(' ')
    igpay = []
    for word in splitText:
        if word == "?":
            igpay.append(word)
        elif word == "!":
            igpay.append(word)
        else:
            word = word+word[0]+'ay'
            word = word[1:]
            igpay.append(word)
    return(' '.join(igpay))

phrase = pig_it(text)
print (phrase)

'''
way better examples

def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])

def pig_it(text):
    res = []
    
    for i in text.split():
        if i.isalpha():
            res.append(i[1:]+i[0]+'ay')
        else:
            res.append(i)
            
    return ' '.join(res)\
'''