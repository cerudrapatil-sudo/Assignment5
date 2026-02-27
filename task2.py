lst=[]

for i in range(1,11):
    lst.append(i)

first_five_no=lst[0:5]

revers=first_five_no[::-1]

print("------------------------------------------------------")

print("Oringinal list: ",lst)
print("Extracted first five elements: ",first_five_no)
print("Reversed extracted elements : ",revers)

print("------------------------------------------------------")