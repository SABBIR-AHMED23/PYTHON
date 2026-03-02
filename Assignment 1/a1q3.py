word=[]
teachers=open(r'E:\PyThon codes\a1\amth.txt')
for teacher in teachers:
    teacher.strip()
    words=teacher.split()
    for word_list in words:
        if word_list not in word:
            word.append(word_list)
print(word)
word.sort()            
print(word)





