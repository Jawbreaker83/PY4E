# The dir() command lists capabilities.  The capabilities with underscores can be ignored as they 
# are used by Python.  The rest are real operators that the object can perform.  It is like type()
# which tells us something about the variable.

y = list()
print(type(y))
print(dir(y))