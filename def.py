
def f(x) : #f(x) = 2x+1
    return ( x*2 ) + 1

def f2(x) : 
    return ( x**2 ) + ( x*2 ) + 1

def mul(*values) :
    output = 1
    for x in values :
        output = output*x
    return output

print ( f(10))
print()
print ( f2(10))
print()
print( mul(5,7,9,10,0))
