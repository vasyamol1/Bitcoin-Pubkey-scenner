from bitcoin import *
import random

print("Loading...")
with open("pubkey.txt","r") as m:
	add = m.read().split()
add= set(add)
while True:
    ran = random.randrange(20282409603651670423947251286016,30423614405477505635920876929022)
    myhex = "%064x" % ran
    myhex = myhex[:64]
    priv = myhex
    pub = privtopub(priv)
    if str(pub) in add:
        print ("found!!!",pub,myhex)
        s1 = myhex
        s2 = pub
       
        f=open(u"win.txt","a")
        f.write(s1)
        f.write(s2)       
        f.close()
        break
    else:
        print ("searc...",pub)
        ran: ran + 1 
