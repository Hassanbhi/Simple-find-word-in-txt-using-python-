import os
ent = input("Enter th word to find in all txt files in this folder :\n")

def isBinod(filename):
    with open(filename,"r") as f:
        filecontents = f.read()
    if ent in filecontents.lower():
        return True
    else:
        return False
 


value = 0
dir_contents = os.listdir()

for item in dir_contents:
    if item.endswith("txt"):
        print(f"Deteceting {ent} in{item}")
            
        if isBinod(item):
            print(f"***~`{ent} found in {item}!!!&!")
            value +=1 
        else:
            print(f"{ent} not found in {item}")

    print(f"{ent} found in {value} files ")
inh = input()