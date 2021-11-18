a = [1.9,1.99,1.999]
b = [2.1,2.01,2.001]

print("ข้อ 2 ซ้าย")
for i in range(len(a)):
    top = a[i]-2
    under = (a[i]**2)+a[i]-6
    x = top/under
    print(x)

print("ข้อ 2 ขวา")
for i in range(len(b)):
    top = b[i]-2
    under = (b[i]**2)+b[i]-6
    x = top/under
    print(x)


limit_set_left = [0.9,0.99,0.999]
limit_set_right = [1.1,1.01,1.001]

print("ข้อ 3 ซ้าย")
for i in range(len(limit_set_left)):
    top = (3*limit_set_left[i])-3
    under = ((limit_set_left[i])**3)-1
    x = top/under
    print(x)
    

print("ข้อ 3 ขวา")
for i in range(len(limit_set_right)):
    top = (3*limit_set_right[i])-3
    under = ((limit_set_right[i])**3)-1
    x = top/under
    print(x)
