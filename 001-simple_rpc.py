def plus(x,y) :
    yield x
    yield y
    yield x+y

for item  in plus(1,2) :
    print(item)
