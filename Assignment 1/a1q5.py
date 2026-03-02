file=open(r'E:\PyThon codes\a1\mbox.txt')
count=0
lists=[]
for line in file:
    if line.startswith('From '):
        count+=1
        value=str(line.split()[1].strip())
        if value not in lists:
            lists.append(value)
            print(value)
print(count)