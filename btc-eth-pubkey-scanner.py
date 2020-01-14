import random
import hashlib
import binascii
from bit import *
from bit.format import bytes_to_wif
from binascii import hexlify
import eth_keys
from eth_keys import keys

print("Loading...")
with open("btc-eth-pubkey.txt","r") as m:
    add = m.read().split()
add= set(add)

def sha256(hex):   #sha256 function
    sha256_signature = hashlib.sha256(binascii.unhexlify(hex)).hexdigest()
    return sha256_signature

ran = 49254312220870758000927442301188605997050322425547362059682114798994592352884

while ran > 7:
        key1 = Key.from_int(ran)
        wif = bytes_to_wif(key1.to_bytes(), compressed=False)
        key2 = Key(wif)
        caddr = key1.address
        uaddr = key2.address
        saddr = key1.segwit_address
        pub1 = hexlify(key1.public_key).decode()
        pub2 = hexlify(key2.public_key).decode()
        myhex = "%064x" % ran 				#eth from line 21 to 26
        private_key = myhex[:64]
        myhash = sha256(myhex)
        private_key_bytes = bytes.fromhex(private_key)
        public_key_hex = keys.PrivateKey(private_key_bytes).public_key
        public_key_bytes = bytes.fromhex(str(public_key_hex)[2:])
        eaddr = keys.PublicKey(public_key_bytes).to_address()
        if caddr in add:
            print ("found!!!",ran ,caddr)
            s1 = str(ran)
            s2 = caddr
            f=open(u"win1.txt","a")
            f.write(s1)
            f.write(s2)      
            f.close()
            break
        if uaddr in add:
            print ("found!!!",ran,uaddr)
            s1 = str(ran)
            s2 = uaddr
            f=open(u"win2.txt","a")
            f.write(s1)
            f.write(s2)      
            f.close()
            break
        if saddr in add:
            print ("found!!!",ran,saddr)
            s1 = str(ran)
            s2 = saddr
            f=open(u"win3.txt","a")
            f.write(s1)
            f.write(s2)      
            f.close()
            break
        if pub1 in add:
            print ("found!!!",ran, pub1)
            s1 = str(ran)
            s2 = pub1
            f=open(u"win4.txt","a")
            f.write(s1)
            f.write(":"+s2)      
            f.close()
            break
        if pub2 in add:
            print ("found!!!",ran, pub2)
            s1 = str(ran)
            s2 = pub2
            f=open(u"win5.txt","a")
            f.write(s1)
            f.write(":"+s2)      
            f.close()
            break
        if eaddr in add:
            print ("found!!!",private_key, eaddr)
            s1 = private_key
            s2 = eaddr
            f=open(u"win6.txt","a")
            f.write(s1)
            f.write(s2)      
            f.close()
            break
        else:
            print ("...", myhex, caddr, saddr, eaddr, pub1)
            ran = int(myhash,base=16)
