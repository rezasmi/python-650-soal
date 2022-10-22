from multiprocessing.sharedctypes import Value
from typing import KeysView


dict_student={}
n=int(input('how many student: '))
for i in range(1,n+1):
    id_i=int(input('inter student id: '))
    avr_i=int(input('enter student avrage: '))
    dict_student[id_i]=avr_i

max_value=max(dict_student.values())
print(type(max_value))
print(max_value)

print(dict_student)
