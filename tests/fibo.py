# Tuples
# t = (1, 'toto', 2.5)
# # print(t)

# game = {'toto', 2, 'toto'}
# print(game)
#
# a = 1
# b = 0
# while (a < 300):
#     c = b
#     b = a
#     a = c + b
#     print(a)

# Enter number of terms needed                   #0,1,1,2,3,5....
a=int(20)
f=1
s=2
if a<=0:
    print("The requested series is",f)
else:
    print(f,s,end=" ")
    for x in range(2,a):
        next=f+s
        print(next,end=" ")
        f=s
        s=next