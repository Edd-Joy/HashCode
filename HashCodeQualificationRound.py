f = open("C:/Users/admin/Downloads/b_little_bit_of_everything.in", "r")

firstLine = f.readline().split()
pizzaNumber = int(firstLine[0])
twoPersonTeams = int(firstLine[1])
threePersonTeams = int(firstLine[2])
fourPersonTeams = int(firstLine[3])

deliveredPizzas = 0
totalTeams = twoPersonTeams + threePersonTeams + fourPersonTeams
ingredientNumber = -1

twoPersonPizzas = []
threePersonPizzas = []
fourPersonPizzas = []

twoPersonIngredients = []
threePersonIngredients = []
fourPersonIngredients = []

twoTemp = []
threeTemp = []
fourTemp = []

c = f.readline()
if c != EOFError and c != "":
    ingredientNumber = ingredientNumber + 1
    score = 0
    ing = c.split()
    ing.pop(0)
    ing.sort()
    for item in ing:
        if item not in twoPersonIngredients:
            twoPersonIngredients.append(item)
            score = score + 1
    ing.insert(0, ingredientNumber)
    ing.insert(1, 2)
    ing.insert(2, score)
    twoTemp.append(list(ing))

c = f.readline()
if c != EOFError and c != "":
    ingredientNumber = ingredientNumber + 1
    score = 0
    ing = c.split()
    ing.pop(0)
    ing.sort()
    for item in ing:
        if item not in threePersonIngredients:
            threePersonIngredients.append(item)
            score = score + 1
    ing.insert(0, ingredientNumber)
    ing.insert(1, 3)
    ing.insert(2, score)
    threeTemp.append(list(ing))

c = f.readline()
if c != EOFError and c != "":
    ingredientNumber = ingredientNumber + 1
    score = 0
    ing = c.split()
    ing.pop(0)
    ing.sort()
    for item in ing:
        if item not in fourPersonIngredients:
            fourPersonIngredients.append(item)
            score = score + 1
    ing.insert(0, ingredientNumber)
    ing.insert(1, 4)
    ing.insert(2, score)
    fourTemp.append(list(ing))  

while deliveredPizzas < pizzaNumber:
    c = f.readline()
    if c != EOFError and c != "":
        ingredientNumber = ingredientNumber + 1
        ing = c.split()
        ing.pop(0)
        ing.sort()
        twoScore = 0
        threeScore = 0
        fourScore = 0
        if len(twoPersonPizzas)/2 < twoPersonTeams:
            #Deliver Two Person Pizzas
            for item in ing:
                if item not in twoPersonIngredients:
                    twoScore = twoScore + 1

        if len(threePersonPizzas)/3 < threePersonTeams:
            #Deliver Three Person Pizzas
            for item in ing:
                if item not in threePersonIngredients:
                    threeScore = threeScore + 1

        if len(fourPersonPizzas)/4 < fourPersonTeams:
            #Deliver four Person Pizzas
            for item in ing:
                if item not in fourPersonIngredients:
                    fourScore = fourScore + 1

        

        if len(twoPersonPizzas)/2 < twoPersonTeams and twoScore >= threeScore and twoScore >= fourScore:
            for item in ing:
                if item not in twoPersonIngredients:
                    twoPersonIngredients.append(item)         
            ing.insert(0, ingredientNumber)
            ing.insert(1, 2)
            ing.insert(2, twoScore)
            twoTemp.append(list(ing))

        elif len(threePersonPizzas)/3 < threePersonTeams and threeScore >= twoScore and threeScore >= fourScore:
            for item in ing:
                if item not in threePersonIngredients:
                    threePersonIngredients.append(item)                    
            ing.insert(0, ingredientNumber)
            ing.insert(1, 3)
            ing.insert(2, threeScore)
            threeTemp.append(list(ing))

        elif len(fourPersonPizzas)/4 < fourPersonTeams and fourScore >= threeScore and fourScore >= twoScore:
            for item in ing:
                if item not in fourPersonIngredients:
                    fourPersonIngredients.append(item)  
            ing.insert(0, ingredientNumber)
            ing.insert(1, 4)
            ing.insert(2, fourScore)
            fourTemp.append(list(ing))            

    else:
        break    

    if len(twoTemp) == 2:
        for item in twoTemp:
            twoPersonPizzas.append(item)
        twoTemp = []
        deliveredPizzas = deliveredPizzas + 2

    if len(threeTemp) == 3:
        for item in threeTemp:
            threePersonPizzas.append(item)
        threeTemp = []
        deliveredPizzas = deliveredPizzas + 3

    if len(fourTemp) == 4:
        for item in fourTemp:
            fourPersonPizzas.append(item)
        fourTemp = []
        deliveredPizzas = deliveredPizzas + 4

    if len(fourPersonPizzas)/4 >= fourPersonTeams and len(threePersonPizzas)/3 >= threePersonTeams and len(twoPersonPizzas)/2 >= twoPersonTeams:
        break

while len(threePersonPizzas)/3 < threePersonTeams:
    if len(fourTemp) > 0:
        tempPizzas = list(fourTemp)
        for item in tempPizzas:
            score = 0
            ingNum = item[0]
            item.pop(0)
            item.pop(0)
            item.pop(0)
            for ing in item:
                if ing not in threePersonIngredients:
                    score = score + 1
            item.insert(0, ingNum)
            item.insert(1, score)
        tempPizzas.sort(key= lambda x: x[1])

        while len(threeTemp) < 3 and len(tempPizzas) > 0:
            tempPizzas[len(tempPizzas) - 1].insert(1, 3)
            threeTemp.append(tempPizzas[len(tempPizzas) - 1])
            for item in fourTemp:
                if item[0] == tempPizzas[len(tempPizzas) - 1][0]:
                    fourTemp.remove(item)
            tempPizzas.pop(len(tempPizzas) - 1)
        
        if len(threeTemp) == 3:
            for item in threeTemp:
                threePersonPizzas.append(list(item))     
            threeTemp = []
            deliveredPizzas = deliveredPizzas + 3          
    else:
        break

c = f.readline()
remainingPizzas = []
while c != EOFError and c != "":
    ing = c.split()
    ing.pop(0)
    ingredientNumber = ingredientNumber + 1
    twoPersonPizzas.sort(key= lambda x: x[2])
    score = 0
    for item in ing:
        if item not in twoPersonIngredients:
            score = score + 1
    if twoPersonPizzas[0][2] < score:
        pizza = twoPersonPizzas[0]
        twoPersonPizzas.pop(0)
        for item in ing:
            if item not in twoPersonIngredients:
                twoPersonIngredients.append(item)
        ing.insert(0, ingredientNumber)
        ing.insert(1, 2)
        ing.insert(2, score)
        twoPersonPizzas.append(list(ing))
        pizza.pop(1)
        pizza.pop(1)
        remainingPizzas.append(list(pizza))
    else:        
        ing.insert(0, ingredientNumber)
        remainingPizzas.append(list(ing))
    c = f.readline()

count = 0
while count < len(remainingPizzas):
    threePersonPizzas.sort(key= lambda x: x[2])
    ing = list(remainingPizzas[count])
    ingNum = ing[0]
    ing.pop(0)
    score = 0
    for item in ing:
        if item not in threePersonIngredients:
            score = score + 1
    if threePersonPizzas[0][2] < score:
        pizza = threePersonPizzas[0]
        threePersonPizzas.pop(0)
        for item in ing:
            if item not in threePersonIngredients:
                threePersonIngredients.append(item)
        ing.insert(0, ingNum)
        ing.insert(1, 3)
        ing.insert(2, score)
        threePersonPizzas.append(list(ing))
        pizza.pop(1)
        pizza.pop(1)
        remainingPizzas.insert(count, list(pizza))
    count = count + 1

count = 0
while count < len(remainingPizzas):
    fourPersonPizzas.sort(key= lambda x: x[2])
    ing = list(remainingPizzas[count])
    ingNum = ing[0]
    ing.pop(0)
    score = 0
    for item in ing:
        if item not in fourPersonIngredients:
            score = score + 1
    if fourPersonPizzas[0][2] < score:
        pizza = fourPersonPizzas[0]
        fourPersonPizzas.pop(0)
        for item in ing:
            if item not in fourPersonIngredients:
                fourPersonIngredients.append(item)
        ing.insert(0, ingNum)
        ing.insert(1, 4)
        ing.insert(2, score)
        fourPersonPizzas.append(list(ing))
        pizza.pop(1)
        pizza.pop(1)
        remainingPizzas.insert(count, list(pizza))
    count = count + 1


#count = 0
#while count < len(remainingPizzas):
#    twoPersonPizzas.sort(key= lambda x: x[2])
#    ing = list(remainingPizzas[count])
#    ingNum = ing[0]
#    ing.pop(0)
#    score = 0
#    for item in ing:
#        if item not in twoPersonIngredients:
#            score = score + 1
#    if twoPersonPizzas[0][2] < score:
#        pizza = twoPersonPizzas[0]
#        twoPersonPizzas.pop(0)
#        for item in ing:
#            if item not in twoPersonIngredients:
#                twoPersonIngredients.append(item)
#        ing.insert(0, ingNum)
#        ing.insert(1, 2)
#        ing.insert(2, score)
#        twoPersonPizzas.append(list(ing))
#        pizza.pop(1)
#        pizza.pop(1)
#        remainingPizzas.insert(count, list(pizza))
#    count = count + 1

#print(deliveredPizzas)
teamsDelivered = len(twoPersonPizzas)//2 + len(threePersonPizzas)//3 + len(fourPersonPizzas)//4
print(teamsDelivered)
#twoTotalScore = 0
#threeTotalScore = 0
#fourTotalScore = 0

print("2", end= " ")
for item in twoPersonPizzas:
    print(item[0], end= " ")
    #twoTotalScore = twoTotalScore + item[2]
print("\n3", end= " ")
for item in threePersonPizzas:
    print(item[0], end= " ")
    #threeTotalScore = threeTotalScore + item[2]
print("\n4", end= " ")
for item in fourPersonPizzas:
    print(item[0], end= " ")
    #fourTotalScore = fourTotalScore + item[2]

#print("\n", twoPersonPizzas)
#print(threePersonPizzas)
#print(fourPersonPizzas)
#print(twoTemp)
#print(threeTemp)
#print(fourTemp)
#print(len(twoPersonPizzas)/2)
#print(len(threePersonPizzas)/3)
#print(len(fourPersonPizzas)/4)
#print(twoTotalScore * twoTotalScore)
#print(threeTotalScore * threeTotalScore)
#print(fourTotalScore * fourTotalScore)
#print(twoPersonIngredients)
#print(threePersonIngredients)
#print(fourPersonIngredients)
#print(remainingPizzas)        
