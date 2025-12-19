print("Student details")

list1=[]
dict1={}

clg=input("Enter the College/Instituiton/University:")
n=int(input("Enter the class strength:"))
sub_n=int(input("Enter the number of subjects:"))
rep=0

for i in range (sub_n):
    j=input("Enter subject code:")
    j=j.upper()
    dict1[j]=i+1
if len(dict1)==sub_n:
    pass
else:
    for i in range(sub_n-len(dict1)):
        j=input("Enter subject code:")
        j=j.upper()
        dict1[j]=len(dict1)+i
sub_c=dict(dict1)
list2=list(dict1)
class student:
    
    def name(self):
        name=input("Enter name:")
        return (f"Name:{name}")
    
    def age(self):
        age=float(input("Enter age:"))
        if 0<age<300:
            pass 
        else:
            raise ValueError()
        return (f"{age}yrs")
    
    def grade(self):
        grade=input("Enter grade[A,B,C,D,F]:")
        grade=grade.upper()
        if grade in ["A","B","C","D","F"] :
            pass
        else:
            raise ValueError()
        return (f"Grade:{grade}")
    
    def reg_no(self):
        reg=int(input("Enter Register Number(number):"))
        return (f"Reg.no:{reg}")
    
    def sem_no(self):
        sem=int(input("Enter semested(number):"))
        if 0<sem<13:
            pass
        else:
            raise ValueError()  
        return (f"Semester:{sem}")
                                
    def sub_code(self):
        sub=input("Enter subject code(enter the associate number given):")
        sub=sub.upper()
        for i in range (len(sub_c)):
            if sub not in list2:
                pass 
            elif sub in list2:
                return (f"Sub_code:{sub}")

print(clg.upper())
print(list2)
for i in range(n*sub_n):
    s=student()
    list1.append(((s.name(),s.age(),s.grade(),s.reg_no(),s.sem_no(),s.sub_code())))
print(list1)