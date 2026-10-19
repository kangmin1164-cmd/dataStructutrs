from ArrayStack import ArrayStack 

s = ArrayStack(10)

for i in range(1, 6):
    s.push(i)
print("push 5회: ", s)

s.pop()
print('pop 1회:', s)

print('peek :', s.peek())