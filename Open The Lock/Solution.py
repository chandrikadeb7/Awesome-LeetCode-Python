class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead_set = set(deadends)
        if '0000' in dead_set: return -1
        que = collections.deque(['0000'])
        count = 0
        while que:
            for x in range(len(que)):
                tmp = que.popleft()
                if tmp == target: 
                    return count
                for i in range(4):
                    left, mid, right = tmp[:i], int(tmp[i]), tmp[i + 1:]
                    for x in [-1, 1]:
                        s = left + str((mid + x) % 10) + right
                        if not s in dead_set:
                            dead_set.add(s)
                            que.append(s)
            count += 1
        return -1
