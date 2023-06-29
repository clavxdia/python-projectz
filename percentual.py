print ("CALCOLO PERCENTUALE")

print ("se non possiedi un dato inserite no")

print("ESEMPIO: p=10, q tot= 800, q ris= no")

a = input("inserisci quantità percentuale ")
b = input ("inserisci quantità totale ")
c = input ("inserisci quantità risultante ")
risultato=0
scelta=0
bis=0

if c=="no":
    a=float(a)
    b=float(b)
    risultato= (a*b)/100
    print("la quantità risultante è ", risultato)
    scelta= input ("si tratta di una quantità in denaro? ")
    if scelta=="si":
        bis= b-risultato
        print ("il tuo valore scontato è pari a €", bis)



if b=="no":
    a=float(a)
    c=float(c)
    risultato= (c*100)/a
    print("la quantità totale è ", risultato)

if a=="no":
    b=float(b)
    c=float(c)
    risultato= (c/b)*100
    print("la quantità percentuale è ", risultato)

#10% (percentuale) di 800 (quantità totale ) è 80 (quantità risultante)
#40% di .... è 4