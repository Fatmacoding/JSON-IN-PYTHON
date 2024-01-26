# list = ["a", "e", "i", "o", "u"]
# t = []
# dect = {}
# k = 0
# m = 0
# # const = 'ooooocccococococococococoooooccc'
# const = input(' -----> entrer la const :  ')
# for i in range(len(const)):
#     if const[i] == "o" :
#         k += 1
#     if const[i] == "c" :
#         m += 1
# dect['o'] = k
# dect['m'] = m
# print('dect = ' , dect)

# # v = input("entrer voyelles : ")
# # chain = input("entrer chain : ")
# # chain2 =" "
# # for i in range(len(chain)):
# #     t.append(chain[i])
# # print('t = ',t)
# # for i in range(len(t)):
# #     if t[i] in list:
# #         t[i] = v
# # print('t = ',t)
# # for i in range(len(t)):
# #     chain2 += t[i] 
# # print('chain2 = ',chain2)

# **********************************************************************
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

