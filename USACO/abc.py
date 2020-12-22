a_string = input()
a_list = a_string.split()
map_object = map(int, a_list)
list_of_integers = list(map_object)

A = min(list_of_integers)
total = max(list_of_integers)

list_of_integers.remove(total)
list2 = []

for i in range(0,len(list_of_integers)):
    if i == A:
        list2.append(i)

if len(list2) == 2:
    C = total - (2 * A)
    print (A,A,C)
elif len(list2) == 3:
    print (A,A,A)
else:
    list_of_integers.remove(A)
    list_of_integers.remove(max(list_of_integers))
    B = min(list_of_integers)
    C = total - (A + B)
    print (A, B, C)




