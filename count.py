list=['a','n','t','a','a','t','n','n','a','x','u','g','a']
i=0
empty=[]
while i<len(list):
    count=0
    j=i
    duplicate=[]
    while j<len(list):
        if list[i] not in empty:
            if list[i]==list[j]:
                count=count+1
        j=j+1
    duplicate.append(list[i])
    duplicate.append(count)
    empty.append(duplicate)
    i=i+1
print(empty)
