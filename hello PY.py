day=input("How many days?")
print(day)

day=int(day)
weeks=day//7
days=day%7
print("you have",int(weeks), "and",int(days),"left")


input("Hello, What is your name?") 
input("Phone number?")
input("Email adress?")
age=input("age?")
print(age)

age=int(age)
years=int(21)-age

print("Hi,__!")
print("You have", years ," years left until you can drink.")

original_letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key_val=2

original_letters=input("write anything")

print (range(len(input)))


for i in range(len(input)) :
  input_chr=input [i]
  idx=original_letters.index(input_chr)
  tmp=idx+key_val
  print(original_letters)[tmp%len(original_letters)]



