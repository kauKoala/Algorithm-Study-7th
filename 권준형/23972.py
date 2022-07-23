# 오답 풀이 - 틀렸습니다로 출력
import math
k, n = map(int, input().split())
if n <= 1: 
    print(-1)
else:
    val = math.ceil((n*k)/(n-1))
    print(val)

## 정답 풀이 - 통과된 풀이
# k, n = map(int, input().split())
# if n <= 1: 
#     print(-1)
# else:
#     res = (n*k) // (n-1)
#     if (n*k) % (n-1):
#         res += 1
#     print(res)