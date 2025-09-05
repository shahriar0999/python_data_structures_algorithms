# take input with spaces sperated value
strs = input().split(' ')

ans=""
v=sorted(strs)
first=v[0]
last=v[-1]
for i in range(min(len(first),len(last))):
    if(first[i]!=last[i]):
        continue
    ans+=first[i]
print(ans) 

