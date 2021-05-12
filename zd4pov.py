a=str(input('Введите предложение:'))
k = ''
s1=a.split()
b=str('привет')
for i in s1:
    if i not in b:
        k += i+ ' '
print("Слова, отличные от привет:", k)