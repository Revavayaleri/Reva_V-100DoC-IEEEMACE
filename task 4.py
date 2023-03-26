lt = []
n = int(input("enter n:"))
for i in range(0,n):
    t = int(input())
    lt.append(t)

sm = 0
for et in lt:
    sm = sm + et
    print("result:", sm)
