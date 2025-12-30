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
sub_c=list(dict1)

class student:
    
    def name(self):
        name=input("Enter name:")
        return (f"Name:{name}")
    
    def age(self):
        age=float(input("Enter age:"))
        while (age<10 or age>119):
            print("INPUT ERROR RE-ENTER THE INPUT")
            age=float(input("Enter age:"))
        return (f"{age}yrs")     
    
    def grade(self):
        grade=input("Enter grade[A,B,C,D,F]:")
        grade=grade.upper()
        while grade not in ["A","B","C","D","F"]:
            print("INPUT ERROR RE-ENTER THE INPUT")
            grade=input("Enter grade[A,B,C,D,F]:")
        grade=grade.upper()
        return (f"Grade:{grade}")
    
    def reg_no(self):
        reg=int(input("Enter Register Number(number):"))
        return (f"Reg.no:{reg}")
    
    def sem_no(self):
        sem=int(input("Enter semested(number):"))
        while sem<1 or sem>12:
            print("INPUT ERROR RE-ENTER THE INPUT")
            sem=int(input("Enter semested(number):"))
        return (f"Semester:{sem}")
                                
    def sub_code(self):
        sub=input("Enter subject code(enter the associate number given):")
        sub=sub.upper()
        while sub not in sub_c:
            print("INPUT ERROR RE-ENTER THE INPUT")
            sub=input("Enter subject code(enter the associate number given):")
            sub=sub.upper()
        return (f"Sub_code:{sub}")

print(clg.upper())
print(sub_c)
for i in range(n):
    s=student()
    name=s.name()
    age=s.age()
    reg_no=s.reg_no()
    for j in range(sub_n):
        sem_no=s.sem_no()
        sub_code=s.sub_code()
        grade=s.grade()
        list1.append((name,age,reg_no,(sem_no,sub_code,grade)))
#displaying the results 

print('''The format of display is 
Student name,age,reg_no,(semmester number,subject code,grade)
''')
print("********************RESULTS********************")
print("\n")
for i in list1:
    print(i)
