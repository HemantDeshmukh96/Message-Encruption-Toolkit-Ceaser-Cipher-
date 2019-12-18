def main( ):
    valid=True
    while valid:
        key=int(input("Enter the key between(1-25) :"))
        if key>25:
            valid=True
        else:
            valid=False
    return key
def encrupt(key):
    inp=input("Enter the Messege to be Encrupted :")
    string=inp.upper()
    for ch in string:
        ch1=ord(ch)
        if ch1==32:print(" ",end="")
        else:
            base=ch1+key
            if base>90:
                base=base-26
            encrup=chr(base)
            print(encrup,end="")
x=main( )
encrupt(x)