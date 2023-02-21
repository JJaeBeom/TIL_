# 큐
def enqueue(data): # 큐 생성 함수
    global rear
    rear += 1
    queue[rear] = data

def dequeue(): # 큐 
    global front
    front += 1
    return queue[front]

queue = [0] *3
front = -1
rear = -1


rear += 1 # enqueue(1)   << 직접 코드로 구현
queue[rear] = 1        # <<
enqueue(2)
enqueue(3)

print(dequeue())
print(dequeue())
if front != rear: # 안전장치. 남아있으면 출력하라. (비어있으면 출력x)
    print(dequeue())
if front != rear:
    print(dequeue())
if front != rear:
    print(dequeue())
#####append 방식
q = []
q.append(10) #어팬드 방식은 매우매우매우 느리다.
q.append(20)
q.append(30)
print(q.pop(0))
print(q.pop(0))
print(q.pop(0))
###########덱쓰는 법 (double en~~~ queue) 더블 엔디드 큐?
from collections import deque
q1 = deque() #빈 리스트에 어펜드하는거보단 훨 빠르긴함. #
q1.append(100)
q1.append(200)
q1.append(300)
print(q1.popleft())
print(q1.popleft())
print(q1.popleft())
#############

