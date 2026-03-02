file=open(r'E:\PyThon codes\a1\regex-sum-42.txt')
number=[]
for line in file:
    line=line.strip()
    parts=line.split()
    for part in parts:
        if part.isdigit():
            number.append(float(part))
print(sum(number))
print(number)
