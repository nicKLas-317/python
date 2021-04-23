def f(obj):
    print(f"Entrée dans f : {id(obj)}  = {obj}")
    obj += "LULU"
    print(f"Sortie de f : {id(obj)}  = {obj}")

#Immutable
obj = "toto"
print(f"Immutable avt passage : {id(obj)} = {obj}")     #@1 = toto
f(obj)                                                  #@1 = toto
                                                        #@2 = totoLULU
print(f"Immutable après passage : {id(obj)} = {obj}")   #@1 = toto


#Mutable
obj = ["toto"]
print(f"Immutable avt passage : {id(obj)} = {obj}")     #@3 = ["toto"]
                                                        #@3 = ["toto"]
f(obj)                                                  #@3 = ["toto", 'L', 'U', 'L', 'U']
print(f"Immutable après passage : {id(obj)} = {obj}")   #@3 = ["toto", 'L', 'U', 'L', 'U']