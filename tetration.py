import math
import locale
locale.setlocale(locale.LC_ALL, 'en_US')


print "Welcome to an Explanation of Tetration"
print ""
raw_input('Press Enter to Advance')
print ""
print "In order to understand tetration, we must understand exponentiation."
raw_input()
print "To understand exponentiation, we must understand multiplication."
raw_input()
print "To understand multiplication, you guessed it, we must understand addition."
raw_input()
print "--------------------------------------------------------------------------"
print "Addition:"
raw_input()
print "Addition starts with counting."
raw_input()
print "If we add 1 to a n times"
raw_input()
print "a + 1 + 1 + 1 + 1...."
raw_input()
print "We get a + n"
raw_input()
print "--------------------------------------------------------------------------"
print "Multiplication:"
raw_input()
print "If we add a to itself n times"
raw_input()
print "a + a + a + a + ...."
raw_input()
print "We get a x n"
raw_input()
print "--------------------------------------------------------------------------"
print "Exponentiation:"
raw_input()
print "If we multiply a to iteself n times"
raw_input()
print "a x a x a x ....."
raw_input()
print "We get a to the nth power or a ^ n"
raw_input()
print "--------------------------------------------------------------------------"
print "Tetration:"
raw_input()
print "Now, if we take a number a and raise it to the power of itelf."
raw_input()
print "And then one step further and raise that a to the power of a."
raw_input()
print "And we do this n times."
print "a ^ (a ^ (a ^ ...))"
raw_input()
print "We get the nth tetration of a "
raw_input()
print "Tetration gets very big very fast"
raw_input()
print "Let's first look at exponents a ^ n"
raw_input()
print "a = 2, n = 2 : 2 ^ 2 = 2 x 2 = 4"
raw_input()
print "a = 2, n = 3 : 2 ^ 3 = 2 x 2 x 2 = 8"
raw_input()
print "a = 2, n = 4 : 2 ^ 4 = 2 x 2 x 2 x 2 = 16"
raw_input()
print "a = 2, n = 5 : 2 ^ 4 = 2 x 2 x 2 x 2 x 2 = 32"
raw_input()
print "We are all familiar with exponential growth, but just as an example:"
raw_input()
print "If we start with one penny and every day we get double the amount that we had the day before"
raw_input()
print "On day 2 we would have 2 pennies, on day 3, 4 pennies, and so on..."
raw_input()
print "After a single month we would have over 10 million dollars!"
raw_input()
penny = 2 ** 30
dollars = penny * .01
print ("2 ^ 30 = $" + locale.format("%d", dollars, grouping=True))
raw_input()
print "Sign me up for that!"
raw_input()
print "But, tetration is a different animal. Let's explore."
raw_input()
print "Remember tetration is defined as a ^ (a ^ (a ^ ...))"
raw_input()
print "a = 2, n = 2 : 2 ^ 2 = 2 x 2 = 4"
raw_input()
print "a = 2, n = 3 : 2 ^ (2 ^ 2) = 2 ^ (2 x 2) = 2 ^ 4 = 16"
raw_input()
print "a = 2, n = 4 : 2 ^ (2 ^ (2 ^ 2)) = 2 ^ (2 ^ 4) = 2 ^ 16 = 65536"
raw_input()
print "This is a unique number in computing as it is the number of possible values in 16 bits"
raw_input()
print "Now let's look at the 5th tetration of 2."
raw_input()
print "a = 2, n = 5 : 2 ^ (2 ^ (2 ^ (2 ^ 2))) = 2 ^ (2 ^ (2 ^ 4) = 2 ^ (2 ^ 16) = 2 ^ 65536"
raw_input()
tet = 2 ** 65536
print "Are you ready for it????"
raw_input()
print tet
raw_input()
length = len(str(tet))
print "Shit! That is a big number!"
raw_input()
print ("It has " + locale.format("%d", length, grouping=True) + " digits!")
raw_input()
print "This is many times more than the estimated number of ordinary atoms"
print "In the observable Universe which is estimated at 1 x 10 ^ 80 !!"
raw_input()
print "Let's put this in a bit more context. Think about the number of possible ways a deck of cards can be arranged."
raw_input()
cards = math.factorial(52)
galaxy = len(str(cards))
print "The answer is 52 factorial."
raw_input()
print ("or 52! = " + str(cards))
raw_input()
print ("It has " + locale.format("%d", galaxy, grouping=True) + " digits!")
raw_input()
print "If you took this many decks of cards and stacked them up,"
print "The resulting stack would be larger than the diameter of the Milky Way Galaxy!"
raw_input()
print "Factorials grow faster than exponentiation, but much slower that tetration!"
raw_input()
print "Now you might ask: how big is the 6th tetration of 2?"
raw_input()
print "Don't worry, I'm not going to lock up your computer trying to compute it =)"
raw_input()
print "a = 2, n = 6 : 2 ^ (2 ^ (2 ^ (2 ^ (2 ^ 2)))) = 2 ^ (2 ^ 65536) = ???"
raw_input()
print "This number is to big for anyone to understand"
raw_input()
print "If we put one digit on every atom in the universe, we would run out of atoms before making even the most"
print "miniscule amount of progress. No matter how bad you want to know the answer, the truth is, you can't"
raw_input()
print "The End"
raw_input()
print ""
print ""
print ""
print ""
print ""
print ""

