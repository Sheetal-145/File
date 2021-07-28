my_file=open("data.txt", "w")
write_something=my_file.write("Name=Sheetal \nPlace=Kotdwara \nD.O.B=15-09-2000 \nEducation=Graduation \nCurrently=Banglore \nHobbies=Games, Poetry, Writing")
my_file.close()

# new_file=open("data.txt", "r")
# read_this=new_file.read()
# print(read_this)


again=open("data.txt", "a")
write_new=again.write(" I am declaring all the details")
again.close()

read_again=open("data.txt","r")
read_2=read_again.read()
print(read_2)

c=0
for i in read_2:
    if i == "\n":
        c+=1
print(c+1)


 
