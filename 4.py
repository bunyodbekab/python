in_info = str(input()).split() #input for user test

def three(a): #main function
    a.sort()
    es = 'a'
    score='1'
    for i in a:
        if i==es:
            score+=1
        elif score==3:
            if es!=1:
                print(es)
            score=1
        else:
            score=1
        es=i

three(in_info) #run function