from collections import deque

soobin, brother = map(int,input().split())
visited = [10 ** 5] * (10 ** 5 + 1) 

def BFS():
    global visited
    visited[soobin] = 0
    queue = deque()
    queue.append(soobin)

    while queue:
        resent_soobin = queue.popleft()
        if 0 <= resent_soobin * 2 <= 10 ** 5:
            if visited[resent_soobin * 2] > visited[resent_soobin] + 1:
                visited[resent_soobin * 2] = visited[resent_soobin] + 1
                queue.append(resent_soobin * 2)

        if 0 <= resent_soobin + 1 <= 10 ** 5:
            if visited[resent_soobin + 1] > visited[resent_soobin] + 1:
                visited[resent_soobin + 1] = visited[resent_soobin] + 1
                queue.append(resent_soobin + 1)

        if 0 <= resent_soobin - 1 < 10 ** 5:
            if visited[resent_soobin - 1] > visited[resent_soobin] + 1:
                visited[resent_soobin - 1] = visited[resent_soobin] + 1
                queue.append(resent_soobin - 1)

BFS()

print(visited[brother])