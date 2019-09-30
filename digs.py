units={0: '',1:'one',2: 'two',3: 'three',4:'four',5: 'five',6: 'six',7: 'seven',8: 'eight',9: 'nine',10: 'ten',11:'eleven',12: 'twelve',13: 'thirteen',14:'fourteen',15: 'fifteen',16: 'sixteen',17: 'seventeen',18: 'eighteen',19: 'nineteen'}
tens={1:'ten',2: 'twenty',3: 'thirty',4:'forty',5: 'fifty',6: 'sixty',7: 'seventy',8: 'eighty',9: 'ninety'}
while(1):
    th1wrds=""
    h1wrds=""
    t1wrds=""
    u1wrds=""
    print("*"*100)
    n=int(input("Please enter a number : "))
    unit1=n%10
    u1=int(float(unit1))
    ten1=(n/10)%10
    t1=int(float(ten1))
    hundred1=(n/100)%10
    h1=int(float(hundred1))
    thousand1=n/1000
    th1=int(float(thousand1))

    ##print("Units",u1)
    ##print("Tens",t1)
    ##print("Hundrends",h1)
    ##print("Thousand",th1)
    if(th1!=0):
        th1wrds=units[th1]+" thousand "
    if(h1!=0):
        h1wrds=units[h1]+" hundred "
    if(t1!=0):
        t1wrds=tens[t1]+" "
    if(u1!=0):
        u1wrds=units[u1]+" "
    if(t1==1):
        t1wrds=units[(t1*10)+u1]
        u1wrds=""
    numwrds=th1wrds+h1wrds+t1wrds+u1wrds
    print(n,"=",numwrds)

