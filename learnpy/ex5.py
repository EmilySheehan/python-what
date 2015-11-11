name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
centimeters_in_inches = 2.54
kilometers_in_pound = 0.453592

print "Let's talk about %s." % kilometers_in_pound
print "He's %s inches tall." % round(height * centimeters_in_inches)
print "He's %s pounds heavy." % (weight * kilometers_in_pound)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)