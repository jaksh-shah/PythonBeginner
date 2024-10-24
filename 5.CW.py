##num1 = min(2.5, 0, -10, int("15")) 
##num2 = max( 1, round(4.1), 12) 
##print(sum(num1, num2))
#-----------------------------------------------------------------------------------------------------------------------------------------------------
##a = 3
##b =4
##c=4
##print(a!=b)
#-----------------------------------------------------------------------------------------------------------------------------------------------------
##s = "Hello World"
##print("Hello" not in s)
#-----------------------------------------------------------------------------------------------------------------------------------------------------
##a1 = 4<9
##a2 = "hello" in "hello world"
##
##print(a1 and a2)
##print(True or False or False)
#-----------------------------------------------------------------------------------------------------------------------------------------------------
##print( True and False)
##                                                                    # This will print False, since both sides are not True
##print( True or False)                                                                    # This is True since one side is True
##print( False and False)                                                                     # What will these print?:1.False
##print( False or False)                                                                                                          #2.False
##print( True or True)                                                                                                             #3.True
##boolean = True and True                             # what will be stored in this variable?:"True" will be saved in this variable.
#------------------------------------------------------------------------------------------------------------------------------------------------------
##print( 12 == 12 and "cat" in "catastrophe")
### 12 == 12 is True, "cat" in "catastrophe" is True
### True and True gives us True
##print( 3 > 5 or 9 > 5)
### 3 > 5 is False, 9 > 5 is True, False or True gives us True
##name = "Samuel"
##age = 14
##print( "u" in name and age < 10)
###"u" in name is asking if there is a "u" in "Samuel", True
### age < 10 is False since age is 14, True and False = False
##print("j" in name or age == 14)             # Solve this one yourself!:It will print "True"
#====================================Classwork Questions======================================
#1.
#   false    true
#   true     true
#   false    true
#2.
#   false   true
#   true    true
#   true    true
#3.
##letter = input("enter a uppercase or lowercase letter.")
##print(letter in "abcdefghijklmnopqrstuvwxyz")
#4.
a=5
b=1
c=0
print(a == b + 3 or a + 5 != 12) and (a + b < 100 and b > c)
