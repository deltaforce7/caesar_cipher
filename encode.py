original_letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key_val=2

letters=input("write anything:")
letters=letters.upper()
print (range(len(original_letters)))


for i in range(len(letters)) : 
  input_chr=letters [i]
  #print (input_chr)
  idx=original_letters.index(input_chr)
  tmp=idx+key_val
  print(original_letters[tmp%len(original_letters)])

  #input to encrypt the output. 
