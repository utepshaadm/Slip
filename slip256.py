''' Slip256 Cipher'''
''' by KryptoMagick (Karl Zander) '''
from random import shuffle

class SLIP256:
    def __init__(self):
        self.deck = list(range(256))
        
    def gen_rand_decks(self):
    	shuffle(self.deck)
    	
    def ksa(self):
         self.deck.append(self.deck.pop(0))
         self.deck.append(self.deck.pop(0))
         
         posA = self.deck[0]
         posB = self.deck[1]
         self.deck[posA], self.deck[posB] = self.deck[posB], self.deck[posA]
         return self.deck[self.deck[posA]] % 256
         
    def encrypt_letter(self, letter):
        num = ord(letter)
        key = self.ksa()
        num = (num ^ key)
        return chr(num)
        
    def decrypt_letter(self, letter):
        num = ord(letter)
        key = self.ksa()
        num = (num ^ key)
        return chr(num)

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
