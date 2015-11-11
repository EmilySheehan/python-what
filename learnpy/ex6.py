x = "There are %d types of people." % 10 #I'm trying to comment on what is happeneing here
binary = "binary"  #this is a string saved as a variable
do_not = "don't" #this is a short variable for a string too
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e