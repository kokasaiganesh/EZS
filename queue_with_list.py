def enqueue():
    print("enter the element:")
    a=input()
    que.append(a)
    print(que)
def dequeue():
    if not que:
        print("queue is empty")
    else:
        a=que[0]
        print("the deleted element is:",a)
        que.pop(0)
        if not que:
            print("queue is empty")
        else:
            print(que)
que=[]
while(1):
    print("enter the option 1.push 2.pop 3.exit")
    x=int(input())
    if x==1:
        enqueue()
    elif x==2:
        dequeue()
    elif x==3:
        exit(0)
    else:
        print("enter the correct option")