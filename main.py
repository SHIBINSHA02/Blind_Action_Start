


dic={}

  
    
    

from art import logo
print(logo)
other_blinder=True
while other_blinder:
    name=input("what is your name.")
    bid=int(input("what is your bid.$"))
    NewInPut=input("yes or no").lower()
    dic[name]=bid
    
    if NewInPut=="no":
        other_blinder=False
      
value1=0 
winner=""       
for key in dic:
    value=dic[key]
    if value>value1:
        value1=value
        winner=key

print(f"{winner} his bid is{value1}")    






