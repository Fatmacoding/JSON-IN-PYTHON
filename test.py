import random
import json

fichier = open('testpython.json' , 'r')
list = json.loads(fichier.read( ))
print(list)
while True :
    choix = int(input('for add tap 1 for remove tap 2 for random tap 3 for stop tap 4 for delet array tap 5:  ' ))
    if choix == 1 :
        n = input(' ---> add world :  ')
        list.append(n)
        print(list)

    elif choix == 2 :
        n = input(' ---> remove world :  ')
        if n in list :
            list.remove(n)
            print(list)
        else :
            print('that world not her .')

    elif choix == 3:
        index = random.randint(0,len(list)-1)
        print(list[index])

    elif choix == 4 :
        print(list)
        break

    else :
        del list
        print('list = []')
        break
    
g = open('testpython.json' , 'w')
g.write(json.dumps(list))
g.close()       

