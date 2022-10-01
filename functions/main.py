# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line
def greet(x):
 greeting = f'Hello, {x}!'
 return greeting
print(greet('Bob'))

#Takes three numbers (int and floats) and returns their sum
def add(x,y,z):
 addition = x + y + z
 return addition

print(add(5,3,2))

#Positive: takes number (int and float) and returns in the form of a boolean
def positive(x):
 if x > 0:
  is_positive = True
  return is_positive
 else:
  is_positive = False
  return is_positive

print(positive(50))
print(positive(0))
print(positive(-50))

"""
Negative: takes a number (integer or float) and returns whether or not it is negative in the form of a boolean. You do not have to handle the case where the argument is not an int or float. Examples:
>>> negative(50)
False
>>> negative(-50)
True
>>> negative(0)
False
""" 

def negative(x):
 if x < 0:
  is_negative = True
  return is_negative
 else:
  is_negative = False
  return is_negative

print(negative(50))
print(negative(0))
print(negative(-50))