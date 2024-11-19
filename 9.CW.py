##name = input("What is your name?")
##letter = input("What is your favourite letter?")
##letter_count = 0
##vowel_count = 0
##for char in name:
##    if char == letter:
##        letter_count += 1
##    if char in "aeiouAEIOU":
##        vowel_count += 1
##print("You have", letter_count,\
##"instances of your favourite letter", letter,"in your name!")
##print("You have", vowel_count, "vowels in your name.")
##print("The total length of your name is", len(name))


##i=1
##while i < 10:
##    print(i)
##    i = i + 1



##age = 0
##while age < 100:
##        age += 1
##print(age)

##num = 0
##while num != 2:
##num += 2


##number_hippos = 1
##more_hippos = "yes"
##while more_hippos == "yes":
##    number_hippos += 1
##    print("You have", number_hippos, "hippos!")
##    more_hippos = input("Do you want another hippo?")


##name = "Rumplestiltskin"
##guess = "John"
##while guess != name:
##        print("I challenge you to guess my name!")
##        guess = input("Enter your guess: ")
##print("Wow! You got it!")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>loops that never stop<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
##game_completed = True
##while not game_completed:
##    print("Keep playing!")


##dollars = 35
##while dollars < 20:
##        print("Insufficient funds.")


##x = 100
##while x != 300:
##        x = x - 5
##guess = "x"


##secret_letter = "b"
##while guess != secret_letter:
##print("Wrong letter! Guess again!")


##cheer = "yes"
##while cheer == "yes":
##        for i in range(3):
##            print("Hip hip hooray!")
##        cheer = input("Would you like us to cheer for you again?")
#>>>>>>>>>>>>>>>>>>>>>>>>>>no more codes that never stop<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}put "break" if you want to stop an ifnint loop{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{
##for i in range(20): # it seems it will repeat 20 times
##    print(i)
##    if i == 10: # but once i is 10, we break out of the loop
##        break


##name = "Rumplestiltskin"
##guess = "wrong guess"
##while guess != name:
##        guess = input("Enter a guess for my name: ")
##        if guess == "I give up!":
##                break
#}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}end of the exampls{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{

#==============================Class Questions=======================================
#1.
##cheer = "yes"
##while cheer == "yes":
##        for i in range(3):
##            print("Hip hip hooray!")
##        cheer = "yes"


#2.
##while 100000000000000000000000000>1000000000000000000000000000000000000000000000000000000000
##         print("hi")

#3.
##word = "obbkcao"
##guess = input("Guess my word")
##while word != guess:
##    guess = input("Guess my word")
     
#4.
##word = "obbkcao"
##guess = input("Guess my word")
##while word != guess:
##    guess = input("Guess my word")
##    if guess == "I give up":
##            break

#5.
##num = int(input("Enter a number:"))
##while num % 2 != 0 :
##        num = int(input("Enter a number:"))


#6.
##for i in range(1,9):
##        print(i)

#7.
##guess = int(input("Guess the number of marbles in the jar: "))
##number_of_marbles = 249
##while guess != number_of_marbles:
##        print("Incorrect guess! Try again!")
