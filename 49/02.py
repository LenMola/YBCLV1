n = int(input(':'))
s = 0
for i in range(2,n+1):
    if n % i == 0:
        s += 1
        print(i)
print('t:',s)

# 8:2^3  3
# 36:2^2*3^2  8
# 16:2^4 4
# 126:2*3*21    11


