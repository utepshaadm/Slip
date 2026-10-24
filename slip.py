''' Slip Card Cipher'''
''' by KryptoMagick (Karl Zander) '''
from random import shuffle

class SLIP:
    def __init__(self):
        self.deck = list(range(52))
        
    def gen_rand_decks(self):
    	shuffle(self.deck)
    	
    def ksa(self):
         self.deck.append(self.deck.pop(0))
         self.deck.append(self.deck.pop(0))
         self.deck.append(self.deck.pop(0))
        
         p = self.deck[1]
         self.deck[0], self.deck[p] = self.deck[p], self.deck[0]
         return self.deck[self.deck[self.deck[p]]] % 26
         
    def encrypt_letter(self, letter):
        num = ord(letter) - 65
        key = self.ksa()
        num = (num + key) % 26
        return chr(num + 65)
        
    def decrypt_letter(self, letter):
        num = ord(letter) - 65
        key = self.ksa()
        num = (num - key)
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
