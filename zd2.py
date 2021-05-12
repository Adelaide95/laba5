s=input('')
d=0
f=0
z=-1
i=len(s)
d=s.find('чу')
f=s.find('щу')
if d > z and f > z:
    if f > d:
        print('первое вхождение:', d)
    else:
        print('второе вхождение:', f)
if f and d==z:
    print('no')