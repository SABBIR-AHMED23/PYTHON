file=open(r'E:\PyThon codes\a1\mbox.txt')
count=0
lists={}
for line in file:
    if line.startswith('From '):
        count+=1
        value=str(line.split()[1].strip())
        if value in lists:
            lists[value]+=1
        else:
            lists[value]=1       
print(count)
print(lists)