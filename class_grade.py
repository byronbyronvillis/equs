mark = input("What is your mark?: ")

try:
   mark_num= int(mark)
except:
   print("this is wrong mate!")
   exit(1)   

if mark_num == 100:
   print("Congrats")
elif mark_num >= 85:
   print("HD")
else:
   print("F")
