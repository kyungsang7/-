import sys
input = sys.stdin.readline

n = int(input())
nums = sorted(list(map(int,input().split())))
p1, p2 = 0, n-1
ans1, ans2 = 0,n-1
min_num = abs(nums[0] + nums[n-1])

while p1 < p2:
    res = nums[p1] + nums[p2]
    if abs(res) < min_num:
        min_num = abs(res)
        ans1, ans2 = p1, p2
    if res < 0:
        p1 += 1
    else:
        p2 -= 1

print(nums[ans1], nums[ans2])