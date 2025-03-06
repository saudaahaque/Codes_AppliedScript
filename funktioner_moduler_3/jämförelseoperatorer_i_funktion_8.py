#Övning 8: Jämförelseoperatorer i funktioner
  
def största_talet(x,y):
    if x > y:
        return x
    else:
        return y
    
resultat = största_talet(40,20)
print("Det största talet är:", resultat)

#Håkans
def biggest_number(a ,b):
    return a if a > b else b

print(biggest_number(10,20))
    
    

