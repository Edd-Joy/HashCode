import time

start_time = time.time()
print("These are the various combinations\n")

f = open("a_example", "r")
arr = f.read().splitlines()

M = int(arr[0][0])
for i in range (0, M +1):
    arr[i] = arr[i].split()

T2 = int(arr[0][1])
T3 = int(arr[0][2])
T4 = int(arr[0][3])

combi = [1,1,0]
IngrediArr = [[0]*M for i in range(M) ]


print(arr)
print("DiffScore Calculation Matrix")
print("  \t1\t2\t3\t4\t5")
for i in range (1,M + 1):   ## Pizza count column
    print(i, end='')
    for j in range (1, M + 1):   ## Pizza count row
       
        DiffScore = 0
        
        for k in range (1, int(arr[i][0]) + 1): ## each elements in i'th pizza

                if ((arr[i][k]) not in arr[j]):
                    DiffScore = DiffScore + 1
                else:
                    continue
        print('\t' + str(DiffScore), end='')
        IngrediArr[i - 1][j - 1] = DiffScore
    print()

print(IngrediArr) ##Diffscore Matrix stored into this array

## For finding 2 Team Pizza Array
## i,e generate an array with DiffScore coressponding to used Pizzas
print("\n\nTwo Array\n")
TwoTeamArr = [[0]*M for i in range(M)]

for i in range (0, M):
    for j in range (0, M):
        TwoTeamArr[i][j] = IngrediArr[i][j] + IngrediArr[j][i]  ## T2 Matrix Stored
        print('\t' + str(TwoTeamArr[i][j]), end='')
    print()

print(TwoTeamArr)

## Representing it to a simpler array
T2best = []

for i in range (0, M):
    for j in range (i, M):
        if (TwoTeamArr[i][j] > 0):
            T2best.append(str(TwoTeamArr[i][j]) + ' ' + str(i+1) + ' ' + str(j+1))
        else:
            continue
for i in range (0, len(T2best)):
    T2best[i] = T2best[i].split()
#print(T2best)  ## It has DiffScore along with pizzas for T2 #####MAIN-1


## Combinations Generator
T4Combi = []  ## 4 teams
for i in range (1, M + 1):
    for j in range (i+1, M + 1):
        for k in range (j+1, M + 1):
            for l in range (k+1, M + 1):
                T4Combi.append(str(i) + ' ' + str(j) + ' ' + str(k) + ' ' + str(l))

print("T4Combi")
print (T4Combi)

T3Combi = []  ## 3 Teams
for i in range (1, M + 1):
    for j in range (i+1, M + 1):
        for k in range (j+1, M + 1):
            T3Combi.append(str(i) + ' ' + str(j) + ' ' + str(k))
print("T3Combi")
print(T3Combi)

## For finding 3 Team Pizza Array
T3best = []
for i in T3Combi:
    temp = i.split(' ') ## Extract Pizza numbers
    p1 = (int(temp[0]))
    p2 = (int(temp[1]))
    p3 = (int(temp[2]))

    p1_p2_sum = int(arr[p1][0]) + int(arr[p2][0])
    p2_p3_sum = int(arr[p2][0]) + int(arr[p3][0])
    p3_p1_sum = int(arr[p3][0]) + int(arr[p1][0])

    SumOfIngredients = int(arr[int(p1)][0]) + int(arr[int(p2)][0]) + int(arr[int(p3)][0])

                   #AuBuC                       #AnB + BnC + CnA 
    DiffScore_3 = SumOfIngredients - ((p1_p2_sum - TwoTeamArr[p1 -1][p2 -1]) + \
                                        (p2_p3_sum - TwoTeamArr[p2 -1][p3 -1]) + \
                                        (p3_p1_sum - TwoTeamArr[p3 -1][p1 -1]))
                                        
    if (DiffScore_3 < 0): ## case if AnBnC exists i,e same ingredient in 3 pizza
        DiffScore_3 = DiffScore_3 + ((DiffScore_3 * -1) * 3)
    T3best.append(str(DiffScore_3) + ' ' + str(p1) + ' ' + str(p2) + ' ' + str(p3))
print(T3best)

## For finding 4 Team Pizza Array
T4best = []
for i in T4Combi:
    temp = i.split(' ') ## Extract Pizza numbers
    p1 = (int(temp[0]))
    p2 = (int(temp[1]))
    p3 = (int(temp[2]))
    p4 = (int(temp[3]))

    p1_p2_sum = int(arr[p1][0]) + int(arr[p2][0])
    p2_p3_sum = int(arr[p2][0]) + int(arr[p3][0])
    p3_p4_sum = int(arr[p3][0]) + int(arr[p4][0])
    p4_p1_sum = int(arr[p4][0]) + int(arr[p1][0])
    p2_p4_sum = int(arr[2][0]) + int(arr[p4][0])
    p1_p3_sum = int(arr[p1][0]) + int(arr[p3][0])

    SumOfIngredients = int(arr[p1][0]) + int(arr[p2][0]) + int(arr[p3][0]) + int(arr[p4][0])


    DiffScore_4 = SumOfIngredients - ((p1_p2_sum - TwoTeamArr[p1 -1][p2 -1]) + \
                                        (p2_p3_sum - TwoTeamArr[p2 -1][p3 -1]) + \
                                        (p3_p4_sum - TwoTeamArr[p3 -1][p4 -1]) + \
                                        (p4_p1_sum - TwoTeamArr[p4 -1][p1 -1]) + \
                                        (p2_p4_sum - TwoTeamArr[p2 -1][p4 -1]) + \
                                        (p1_p3_sum - TwoTeamArr[p1 -1][p3 -1]))

    if (DiffScore_4 < 0): ## case if AnBnCnD exists
        DiffScore_4 = DiffScore_4 + ((DiffScore_4 * -1) * 4)
    elif (DiffScore_4 == 0):
        DiffScore_4 = (DiffScore_4 + 3)
    T4best.append(str(DiffScore_4) + ' ' + str(p1) + ' ' + str(p2) + ' ' + str(p3) + ' ' + str(p4))
print(T4best)

## Scoring




print("--- %s seconds ---" % (time.time() - start_time))