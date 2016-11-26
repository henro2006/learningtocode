import time
#this is my note
my_number = 700
#float=decimal
my_float = 7.1
# this is a string
my_string = 'henro'
# non literal string
my_non_literal_string = "luis"

# primitive collection types
# list
# aka array
my_list = [
    my_string,
    my_non_literal_string,
    "heaven",
    "slim shady"
]

#dictionary
#aka hash array
my_dictionary = {
    "name" : "henry",
    "height" : "7ft",
    "weight" : "120"
}

# control structures
# this is a for loop
#for name in my_list:
#    if name == "luis":
#        print "sorry, luis is not allowed here!"
#        exit(1)
#    print "hi! my name is {0}".format(name)

# this is a while loop
#number = 0
#while number < 5:
#    print "I am going on forever"
#    time.sleep(1)
#    number = number + 1

class Dog(object):
    def __init__(self, age, size, name, breed):
        self.age = age
        self.size = size
        self.name = name
        self.breed = breed

class Cat(object):
   def __init__(self, age, size, name, breed):
       self.age = age
       self.size = size
       self.name = name
       self.breed = breed

my_sueage = Dog(
    13,
    "small",
    "sueage",
    "chihuahua"
)
my_baya = Dog(
    9,
    "large",
    "baya",
    "boxer"
)
print my_sueage.age
print my_sueage.size
print my_sueage.name

print my_baya.age
print my_baya.size
print my_baya.name
my_kitty_meow = Cat(
    12,
    "small",
    "kitty meow",
    "mutt"
)

print my_kitty_meow.age
print my_kitty_meow.size
print my_kitty_meow.name
