my_file=open("new.txt", "w")
banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
i=0
while i<len(banks_list):
    my_file.write(banks_list[i])
    my_file.write("\n")
    i+=1
my_file.close()

mine=open("new.txt", "r")
reed=mine.read()
print(reed)
