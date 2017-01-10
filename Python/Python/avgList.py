# print the average of all the values in the list: a= [1,2,5,10,255,3]
a = [1,2,5,10,255,3]
sum = 0
for count in range(0,6):
    sum += a[count]
avg = sum/len(a)

print avg

