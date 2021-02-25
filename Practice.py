def AssignPizzas1(M, T2, T3, T4):
    rem = -1
    two = 0
    three = 0
    four = 0
    q = 0

    while(rem != 0):

        if(M%9==0):
            q = M/9
            for i in range (0,int(q)):
                two = two +1
                three = three +1
                four = four +1
            break
        elif(M%7==0):
            q = M/7
            for i in range (0,int(q)):
                four = four + 1
                three = three + 1
            break
        elif(M%5==0):
            q = M/5
            for i in range (0,int(q)):
                two = two + 1
                three = three + 1
            break
        elif (M%3==0):
            q = M/3
            for i in range (0,int(q)):
                three = three + 1
            break
        else:
            print("\t\t\t\t\tUhm !!!")
            break
    print("{0}\t{1}\t{2}\t{3}".format(M, two, three, four))

#def AssignPizzas2(M, T2, T3, T4):

f = open("a_example", "r")
str = f.read().splitlines()
print(str)
M = int(str[0][0])
T2 = int(str[0][2])
T3 = int(str[0][4])
T4 = int(str[0][6])

print("M\t2\t3\t4")
#for i in range (0,200):
AssignPizzas1(M, T2, T3, T4)
    

#print(M,T2,T3,T4)
#def MaxScore():

