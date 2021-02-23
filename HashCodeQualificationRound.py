f = open("C:/Users/admin/Downloads/a_example", "r")

firstLine = f.readline().split()
pizzaNumber = int(firstLine[0])
twoPersonTeams = int(firstLine[1])
threePersonTeams = int(firstLine[2])
fourPersonTeams = int(firstLine[3])

totalTeams = twoPersonTeams + threePersonTeams + fourPersonTeams
ingredientNumber = -1
deliveredPizzas = 0
remainingPizzas = []

def deliverPizzas(persons, teams, pizzas):
    global ingredientNumber
    global deliveredPizzas

    temp = []
    ingredients = []

    while deliveredPizzas < pizzaNumber and len(pizzas) < teams:
        ingredients_cpy = list(ingredients)

        c = f.readline()
        if c != EOFError and c != "":
            match = False
            ingredientNumber = ingredientNumber + 1
            ing = c.split()
            ing.pop(0)
            for item in ing:
                if item not in ingredients_cpy:
                    ingredients_cpy.append(item)
                else:
                    match = True                    
                    for pizza in remainingPizzas:
                        m = False
                        ingredients_cpy = list(ingredients)
                        for pizza_ing in range(1, len(pizza)):
                            if pizza[pizza_ing] not in ingredients_cpy:
                                ingredients_cpy.append(pizza[pizza_ing])  
                            else:
                                m = True
                        if m != True:
                            temp.append(list(pizza))
                            ingredients = list(ingredients_cpy)
                            break
                    break
            
            ing.insert(0, ingredientNumber)
            if match == False:
                temp.append(list(ing))
                ingredients = list(ingredients_cpy)
            else:
                remainingPizzas.append(list(ing))

            if len(temp) == persons:                
                for item in temp:
                    pizzas.append(item)
                    if item in remainingPizzas:
                        remainingPizzas.remove(item)
                temp = []
                ingredients = []
                deliveredPizzas = deliveredPizzas + persons

        else:
            if len(temp) > 0:
                for item in temp:
                    for item_ing in range(1, len(item)):
                        if item[item_ing] in ingredients:
                            ingredients.remove(item[item_ing])
                    if item not in remainingPizzas:
                        remainingPizzas.append(item)                                                
                    
            break


def checkRemainingPizzas(persons, teams, pizzas):
    global remainingPizzas
    
    temp = []
    i = 0
    while (len(remainingPizzas) + len(temp)) >= persons and len(pizzas)/persons < teams:
        ingredients = []
        remPizza_cpy = []

        for item in remainingPizzas:
            remPizza_cpy.append(list(item))

        for item in temp:
            for item_ing in range(1, len(item)):
                if item[item_ing] not in ingredients:
                    ingredients.append(item[item_ing])

        for item in remPizza_cpy:
            score = 0
            for item_ing in range(1, len(item)):
                if item[item_ing] not in ingredients:
                    score = score + 1
            item.insert(0, score)

        remPizza_cpy.sort(key= lambda x: x[0])
        for item in range(len(remPizza_cpy) - 1, -1, -1):
            ing = list(remPizza_cpy[item])
            ing.pop(0)
            if ing not in temp:
                break
                      
        temp.append(ing)      

        if len(temp) == persons:
            for item in temp:
                for pizza in remainingPizzas:
                    if pizza[0] == item[0]:
                        remainingPizzas.remove(pizza)
                pizzas.append(item)
            temp = []

        i = i + 1


twoPersonPizzas = []
threePersonPizzas = []
fourPersonPizzas = []

deliverPizzas(2, twoPersonTeams, twoPersonPizzas)
deliverPizzas(3, threePersonTeams, threePersonPizzas)
deliverPizzas(4, fourPersonTeams, fourPersonPizzas)

c = f.readline()
while c != EOFError and c != "":
    ingredientNumber = ingredientNumber + 1
    ing = c.split()
    ing.pop(0)
    ing.insert(0, ingredientNumber)
    remainingPizzas.append(ing)
    c = f.readline()

if len(remainingPizzas) > 0:
    if(len(twoPersonPizzas)/2 < twoPersonTeams):
        checkRemainingPizzas(2, twoPersonTeams, twoPersonPizzas)

    if(len(threePersonPizzas)/3 < threePersonTeams):
        checkRemainingPizzas(3, threePersonTeams, threePersonPizzas)

    if(len(fourPersonPizzas)/4 < fourPersonTeams):
        checkRemainingPizzas(4, fourPersonTeams, fourPersonPizzas)

totalDelivered = len(twoPersonPizzas)//2 + len(threePersonPizzas)//3 + len(fourPersonPizzas)//4

print(totalDelivered)

for i in range(0, len(twoPersonPizzas), 2):
    print("2", twoPersonPizzas[i][0], twoPersonPizzas[i + 1][0])

for i in range(0, len(threePersonPizzas), 3):
    print("3", threePersonPizzas[i][0], threePersonPizzas[i + 1][0], threePersonPizzas[i + 2][0])

for i in range(0, len(fourPersonPizzas), 4):
    print("4", fourPersonPizzas[i][0], fourPersonPizzas[i + 1][0], fourPersonPizzas[i + 2][0], fourPersonPizzas[i + 3][0])
