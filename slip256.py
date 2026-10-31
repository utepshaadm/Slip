''' Slip256 Stream Cipher'''
''' by KryptoMagick (Karl Zander) '''
from os import urandom

class SLIP256:
    def __init__(self):
        self.deck = list(range(256))
        self.c = 0
        
    def gen_rand_key(self, keylen=32):
        return urandom(keylen)
        
    def gen_rand_nonce(self, nonce_len=16):
        return urandom(nonce_len)
        
    def ksa(self, key, nonce):
        for i in range(256):
            self.deck.append(self.deck.pop(0))
            self.deck.append(self.deck.pop(0))
            posA = self.deck[0]
            posB = key[i % len(key)]
            self.deck[posA], self.deck[posB] = self.deck[posB], self.deck[posA]
            
        for i in range(256):
            self.deck.append(self.deck.pop(0))
            self.deck.append(self.deck.pop(0))
            posA = self.deck[0]
            posB = nonce[i % len(nonce)]
            self.deck[posA], self.deck[posB] = self.deck[posB], self.deck[posA]
        self.p = self.deck[0]
        self.q = self.deck[1]
    
    def update(self):
        self.deck.append(self.deck.pop(0))
        self.deck.append(self.deck.pop(0))
        self.p = self.deck[self.deck[self.p]]
        self.q = self.deck[self.deck[self.deck[self.q]]]
        self.deck[self.q], self.deck[self.c] = self.deck[self.c], self.deck[self.q]
        o = self.deck[self.deck[self.deck[self.p]]]
        self.deck[self.p], self.deck[self.q] = self.deck[self.q], self.deck[self.p]
        self.c = (self.c + 1) % 256
        return o
         
    def encrypt_byte(self, b):
        num = ord(b)
        key = self.update()
        num = (num ^ key)
        return chr(num)
        
    def decrypt_byte(self, b):
        num = ord(b)
        key = self.update()
        num = (num ^ key)
        return chr(num)

    def encrypt(self, msg, key, nonce):
        self.ksa(key, nonce)
        ctxt = []
        for x in range(len(msg)):
            b = self.encrypt_byte(msg[x])
            ctxt.append(b)
        return "".join(ctxt)

    def decrypt(self, ctxt, key, nonce):
        self.ksa(key, nonce)
        ptxt = []
        for x in range(len(ctxt)):
            b = self.decrypt_byte(ctxt[x])
            ptxt.append(b)
        return "".join(ptxt)
