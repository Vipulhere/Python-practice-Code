from collections import deque
queue=deque(["python","java","php"])
print(queue)
queue.append("ruby")
print(queue)
print(queue.popleft())
print(queue)
