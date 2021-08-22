#Implementing Caesar Cipher(2 weeks)

# HW 2
# part 1
# - annotate each line on what the code is doing
# - rewrite the caesar cipher procedure with user input
# - push caesar_cipher.py to your github and share the link to your github with me after finished

# part 2
# - print "AP Computer Science" on the terminal 100 times (use loops)


#global variables
original_letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key_val=2

#user_input=input("input: ").upper()

# output=""

# for i in range(len(user_input)):
#     input_chr=user_input[i]
#     idx=original_letters.index(input_chr) 
#     tmp=idx+key_val
#     output+=(original_letters[tmp%len(original_letters)])

# print("output:",output)
#########################################################
 ## Example 1
#no output, # has input but not using inputs
def temp(a,b,c): #define, temp-> function, a,b,c-> parameters, argument or the input
    # block of code or instructions that you want to execute
    # may or may not have an output
    print("hi")


#temp(1,2,3)

########################################################

 ## Example 2
#have output and input
i="hi"
def encode(user_input): #define, temp-> function, a,b,c-> parameters or the input
    user_input=user_input.upper()
    output=""
    for i in range(len(user_input)):
        input_chr=user_input[i]
        idx=original_letters.index(input_chr) 
        tmp=idx+key_val
        output+=(original_letters[tmp%len(original_letters)])
    return output

answer=encode("hi")
#print(encode("summer"))
#print(output) # trashes everything that are output or assigned outside of the function
# those variables that are deleted are called local variables

#Scoping

#########################################################
 ## Example 3
#no output, # has input but not using inputs

def temp(a=0,b=1,c=2): #setting default values for a,b,c
    print("a:",a)
    print("b:",b)
    print("c:",c)


# temp(1,2,3) #1,2,3
# temp() #0,1,2
# temp(1,2) #1,2,2
# temp(b=6,c=4) #1,6,4