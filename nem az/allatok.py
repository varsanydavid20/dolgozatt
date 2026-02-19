class Allatok:
    def __init__(self,név,súly):
        self.név=név
        self.súly=súly
     
Lallatok=[]

for i in range(3):
    név=input("Adja meg az állat nevét: ")
    súly=int(input("Adja meg az állat súlyát: "))
    allat=Allatok(név,súly)
    Lallatok.append(allat)