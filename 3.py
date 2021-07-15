# [2,2,65,56,56,8,89,1,32].sort() | python alredy have got sort() function
a = str(input()).split() #test input

for i in range(0, len(a)): #str list to int list
    a[i]= int(a[i])



def sort(list_): #main function
    for i in range(len(list_)):
        min_idx = i
        for j in range(i+1, len(list_)):
            if list_[min_idx] > list_[j]:
                min_idx = j       
        list_[i], list_[min_idx] = list_[min_idx], list_[i]
    return list_

print(sort(a)) #ru function
