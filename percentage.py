print ("percentage calculation")

print ("if you don't have a variable, enter no")

print("EXAMPLE: p=10, q tot= 800, q ris= no")

a = input("enter percentage amount ")
b = input ("enter total quantity ")
c = input ("enter resulting quantity ")
result=0
choice=0
bis=0

if c=="no":
    a=float(a)
    b=float(b)
    result= (a*b)/100
    print("the resulting quantity is ", result)
    choice= input ("are we talking about money? ")
    if choice=="yes":
        bis= b-result
        print ("your discounted value is €", bis)

if b=="no":
    a=float(a)
    c=float(c)
    result= (c*100)/a
    print("the total quantity is ", result)

if a=="no":
    b=float(b)
    c=float(c)
    result= (c/b)*100
    print("the percentage amount is ", result)

#10% (percentage) of 800 (total quantity ) is 80 (resulting quantity)
#40% of .... is 43
