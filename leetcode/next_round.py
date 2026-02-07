n, k = map(int, input().split())
scores = list(map(int, input().split()))
 
k_val = scores[k-1]
count = 0
for i in range(n):
    if scores[i] >= k_val and scores[i] > 0:
        count += 1
        
print(count)