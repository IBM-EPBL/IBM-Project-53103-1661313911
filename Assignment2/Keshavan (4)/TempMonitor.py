import random
your_temperature=[10,20,30,40,50,60,70,80,90,100]
humidity=[10,20,30,40,50,60,70,80,90,100]
    
temp=random.choice(your_temperature)
humidi=random.choice(humidity)
#print(temp)
#print(humidi)
while((temp)and(humidi)):
    print("temperature = ",temp)
    print("humidity = ",humidi)
    
    if ((temp<15)or(temp>25)or (temp>=15 and temp<=25)):
        if(temp<15):
            print("It feels like Sweaty")
            print("alarm detected-->ring,ring,ring,....\n")
        elif(temp>25):
            print("It feels like Chill/Shiver")
            print("alarm detected-->ring,ring,ring,....\n")
        elif(temp>=15 and temp<=25):
            print("It's a good environment")
            print("keep moving forward\n")
        
        else:
            continue
    if ((humidi<30)or(humidi>60) or (humidi>=30 and humidi<=60)):
        if (humidi<30):
            print("Dry place,it is not good for your health! Please leave from here.")
            print("alarm detected-->ring,ring,ring,....\n")
        elif (humidi>60):
            print("Lots of moisture in the air! Please leave from here.")
            print("alarm detected-->ring,ring,ring,....\n")
        elif(humidi>=30 and humidi<=60):
            print("It's a good environment")
            print("keep moving forward\n")
        else :
            continue
    if ((temp<=15 or temp>=25)and(humidi<=30 or humidi >=60)):
        print("Please avoid to move outside from home\n")
        
    if ((temp>=15 and temp<=25)and (humidi>=30 and humidi<=60)):
        print("Good environment you can enjoy this moment\n")

    Next=input("Please enter 'Y' for continue\nEnter 'N' for close : \n")
    Next.lower()
    if Next=="Y" or Next=="y":
        temp=random.choice(your_temperature)
        humidi=random.choice(humidity)
    elif Next=="N" or Next=="n":
        break
        
  

    
            
            
        
