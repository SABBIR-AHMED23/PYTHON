file=open(r'E:\PyThon codes\a1\students-marks.txt')
print('Roll','\t  Letter Grade','\t      Grade Point')
for marks in file:
    marks=marks.split()
    mark=(int(marks[1])+int(marks[2]))/2+int(marks[3])+int(marks[4])
    if mark>100:
        print('Invalid mark!')
    elif mark>=80:
        print(int(marks[0]),'\t\tA+','\t\t4.00')
    elif mark>=75:
        print(int(marks[0]),'\t\tA','\t\t3.75')
    elif mark>=70:
        print(int(marks[0]),'\t\tA-','\t\t3.50')
    elif mark>=65:
        print(int(marks[0]),'\t\tB+','\t\t3.25')
    elif mark>=60:
        print(int(marks[0]),'\t\tB','\t\t3.00')
    elif mark>=55:
        print(int(marks[0]),'\t\tB-','\t\t2.75')
    elif mark>=50:
        print(int(marks[0]),'\t\tC+','\t\t2.50')
    elif mark>=45:
        print(int(marks[0]),'\t\tC','\t\t2.25')
    elif mark>=40:
        print(int(marks[0]),'\t\tD','\t\t2.00')
    else:
        print(int(marks[0]),'\t\tF','\t\t0.00')   





