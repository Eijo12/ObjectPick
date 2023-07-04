import random
import time

class Rob(object):
    def __init__(self):
        self.collected=[]
        self.nofcollected=0 #number of collected items
        self.dropped=[]
        self.nofdropped=0 #number of dropped items

    def pick(self, number:int, objects): #pick and remember the objects
        for i in range(number):
            self.collected.append(objects[i])
            self.nofcollected+= 1

    def count(self):
        print("Number of Objects: ", self.nofcollected, "\nObjects:", self.collected)

    def drop(self, dobject: str): #drop the object
        if dobject in self.collected:
            self.collected.remove(dobject)
            self.nofcollected-=1
            self.dropped.append(dobject)
            self.nofdropped+=1
        else:
            print("Error")
    def randdrop(self): #drop randomly
        if len(self.collected)!=0:
            a=random.randrange(self.nofcollected)
            dobject=self.collected[a]
            self.collected.remove(dobject)
            self.nofcollected-=1
            self.dropped.append(dobject)
            self.nofdropped+=1
        else:
            print("Error")
        
    def countdrop(self):
        print("Number of Dropped Objects: ", self.nofdropped, "\nDropped Objects:", self.dropped)

robot1=Rob()
while 1:
    print("\nPick Objects (a)\nCount Picked Objects (b)\nDrop an Object (c)\nRandomly Drop an Object (d)\nCount Dropped Objects (e)\nExit (q)")
    op=input("Enter the operation that you want to perform: ")

    if(op=="a"): #Picking objects
        num=int(input("Number of the objects: "))
        obj=[]
        for i in range(num):
            k=input("Enter the " + str(i+1) + ". Object:")
            obj.append(k)
        robot1.pick(num, obj)
        time.sleep(0.5)

        
    elif(op=="b"):
        robot1.count()
        time.sleep(0.5)
    
    elif(op=="c"):
        rmv=input("Enter the object you want to remove: ")
        robot1.drop(rmv)
        time.sleep(0.5)

    elif(op=="d"): #Dropping an object
        robot1.randdrop()
        time.sleep(0.5)

    elif(op=="e"):
        robot1.countdrop()
        time.sleep(0.5)

    elif(op=="q"):
        break