#example1
#create a string variable

'''s="welcome"
s=str("welcome")
#you can use single notation as well

#name=str()      #when you dont know the value of string yet. they are empty sring variable
#name=""

#example 2
#mutable:cannot change the value of variable
#immutable: can change
#String is immutable

str1="welcome" #the computer create a memory for the str1 and store the value there with a particular id

print(id(str1)) #output is 3021261130736

str1=str1+"welcome to python" #another is created for the str1 update which will have another id
print(id(str1))
#if the value of id changes, it is immutable'''

'''str="welcome"
print(str*10) #when * is used with a string, it does multiplication'''

'''#Example 3: slicing []
#starting index 0
#ending index 1
str="welcome"
print(str[1:3]) #output el
print(str[:6]) #welcom
print(str[2:]) #lcome
print(str[1:-1]) #elcom it starts from the first index and then remove the last xter and then combine

#example 4: ord()  and chr()
print(ord(A)) #RETUEN 65, The ASCII code of the character
print(chr(65)) #returns A, THE CHARACTER REPRESENTED BY A ASCII number

#Example5: #max(), min(), len()
print(max("abc")) #returns c
print(min("abc")) #returns a
print(len("welcome")) #returns 7

#Example 7: IN, NOT IN OPERATORS---Returns a boolean value i.e True or False

s="welcome"
print("come" in s) #returns #True
print("lome" in s)   #returns #False



print("come" not in s) #returns #False
print("lome"not in s)   #returns #True

#Example: string comaparison
print("tim"=="tie") #False
print("free"!="tie") #True
print("arrow">"aron") #True it compares the alphabet order, then pick the one that is greater
#Example: tessting string
s = "welcome"
print(s.isalnum()) #out put false
print(s.isalpha()) #Output True
print("".isspace()) #output tru

#Example: searching for substring
s= "welcome to python"
print(s.endswith("thon"))
print(s.startswith("good")) #false

#Example: Converting string
s="String in python"
s1=s.capitalize()
print(s1)  #Ouput String In Python"

#Exmaple: Reversing string
#METHOD1
S="Welcome"
Reverse_s = ""
for i in S:   #get e first, then, m, then o etc
    Reverse_s=i+Reverse_s
    print("resversed string is:", Reverse_s) #output emoclew'''
#METHOD2
S="Welcome"
Reverse_s=S[::-1]
print(Reverse_s) #OUTPUT emocleW





