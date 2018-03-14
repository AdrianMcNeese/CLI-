import os

names = ['ADMIN','Names']
emails = ['admin@gmail.com','Emails']
lps = ['100','LoyaltyPoints']

def get(nm):
    y = names.index(nm)
    return ("{}   {}   {}".format(names[y],emails[y], lps[y]))

def save():
    with open('ClientList.txt','w') as f:
        zippy = zip(names[2:],emails[2:],lps[2:])
        for item in zippy:  
            f.write(' '.join(map(str,item)) +  '\r\n')

def add():
    newname = input("What is your name? ")
    names.append(newname)
    newemail = input("What is your email? ")
    emails.append(newemail)        
    newlp = input("Enter your correct amount of loyalty points: ")
    lps.append(newlp)
    save()
    load()

def view():
    os.startfile('ClientList.txt')

def viewpers(nm):
    y = names.index(nm)
    print(f"{names[y]}   {emails[y]}   {lps[y]}")

def load():
    with open('ClientList.txt','r') as f:
        for line in f:
            data = line.split(' ')
            if len(data) >= 3:
                name, email, lp = data
                names.append(name)
                emails.append(email)
                lps.append(lp)

def has(nm):
    return nm in names

def isadmin(nm):
    return nm == "ADMIN"

def delete(nm):
    y = names.index(nm)
    names.pop(y)
    emails.pop(y)
    lps.pop(y)
    print("Customer deleted!")
    save()

def replace(nm):
    y = names.index(nm)
    a = input("(New) Name: ")
    b = input("(New) Email: ") 
    names[y] = a
    emails[y] = b

def addpoints(nm):
    y = names.index(nm)
    num = input("How many points would you like to add? (NO COMMAS PLEASE)")
    x = str(num) + str(lps[y])
    lps[y] = x

def takepoints(nm):
    y = names.index(nm)
    num = input("How many points would you like to use? (NO COMMAS PLEASE)")
    if int(lps[y]) >= int(num):
        x = int(lps[y]) - int(num)
        lps[y] = x
    else:
        print("Number entered too high. Goodbye!")
        exit()

def update():
    see = input("Updated! Would you like to see? y/n \r\n>")
    if see == "y":
        viewpers(nm)
    else:
        print("Have a great day!") 
        exit()      