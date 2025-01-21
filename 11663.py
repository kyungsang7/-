import sys
input = sys.stdin.readline

N,M = map(int,input().split())
nums = sorted(list(map(int,input().split())))

def bin(num):
    right, left = 0, N-1
    while right <= left:
        mid = (right + left) // 2
        if num >= nums[mid]:
            right = mid + 1
        else:
            left = mid - 1
    return right

for _ in range(M):
    p1, p2 = map(int,input().split())
    a = bin(p1)
    b = bin(p2)

    if p1 in nums:
        print(b-a+1)
    else:
        print(b-a)