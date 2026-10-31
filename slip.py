''' Slip Card Cipher'''
''' by KryptoMagick (Karl Zander) '''
from random import shuffle

class SLIP:
    def __init__(self, key=None):
        if key is not None:
        	self.deck = list(key)
        else:
            self.deck = list(range(52))
        self.p = self.deck[0]
        self.q = self.deck[1]
        self.c = 0
        
    def gen_rand_decks(self):
    	shuffle(self.deck)
    	
    def update(self):
        self.deck.append(self.deck.pop(0))
        self.deck.append(self.deck.pop(0))
        self.p = self.deck[self.deck[self.p]]
        self.q = self.deck[self.deck[self.deck[self.q]]]
        self.deck[self.q], self.deck[self.c] = self.deck[self.c], self.deck[self.q]
        o = self.deck[self.deck[self.deck[self.p]]] % 26
        self.deck[self.p], self.deck[self.q] = self.deck[self.q], self.deck[self.p]
        self.c = (self.c + 1) % 52
        return o
         
    def encrypt_letter(self, letter):
        num = ord(letter) - 65
        key = self.update()
        num = (num + key) % 26
        return chr(num + 65)
        
    def decrypt_letter(self, letter):
        num = ord(letter) - 65
        key = self.update()
        num = (num - key) % 26
        return chr(num + 65)

    def encrypt(self, letters):
        ctxt = []
        for x in range(len(letters)):
            letter = self.encrypt_letter(letters[x])
            ctxt.append(letter)
        return "".join(ctxt)

    def decrypt(self, letters):
        ptxt = []
        for x in range(len(letters)):
            letter = self.decrypt_letter(letters[x])
            ptxt.append(letter)
        return "".join(ptxt)
