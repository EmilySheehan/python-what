print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()
print "and your name is?",
name = raw_input()

def greet(name):
	print "Hello " + name

greet(name)
print "So, you're %s old, %r tall and %r heavy." % (age, height, weight)

