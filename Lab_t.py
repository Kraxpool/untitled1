s = str(input("Enter string: "))
for c in s:
    print(c)
count = 0;
for c in s:
    if c=='a':
        count = count+1
        print("count = ", count)