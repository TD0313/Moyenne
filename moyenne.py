note1 = int(input("Note1 :"))
note2 = int(input("Note2 :"))
note3 = int(input("Note3 :"))
moyenne : note1+note2+note3/3
print ("Votre moyenne est de,")

if moyenne < 10 :
    print ("Insuffisant")
elif moyenne >= 10 and moyenne <= 12 :
    print ("Passable")
elif moyenne >= 12 and moyenne <= 14 :
    print ("Assez bien")
elif moyenne >= 14 and moyenne <= 16 :
    print ("Bien")
elif moyenne >= 16 :
    print ("Excellent")
else:
    print ("N'existe pas")
