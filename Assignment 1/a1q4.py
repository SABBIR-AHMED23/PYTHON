file=open(r'E:\PyThon codes\a1\mbox.txt')
count=0
total=0.0
for line in file:
    if line.startswith('X-DSPAM-Confidence:'):
        value=float(line.split(':')[1].strip())
        total+=value
        count+=1
if count>0:
    average=total/count
else:
    average=0.0
print(count)    
print(f'Average spam confidence: {average:.4f}')    
