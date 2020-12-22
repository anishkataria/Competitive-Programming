N = int(input())
a_string = input()
a_list = a_string.split()
map_object = map(int, a_list)
list_of_integers = list(map_object)

r = []
total = 0

for number in range(1,N):
    for number_second in range(number+1, N+1):
        r.append([number,number_second])




for n in r:
    iterator = 0
    total_petals = []
    for i in range(n[0] - 1, n[1]):
        iterator += list_of_integers[i]
        total_petals.append(list_of_integers[i])
    average_petals = iterator/len(total_petals)
    if average_petals in total_petals:
        total += 1

total += N

print(total)

