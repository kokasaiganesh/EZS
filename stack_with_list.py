def push_element():
    n=input("enter the element:")
    str.append(n)
    print(str)
def pop_element():
    if not str:
        print("stack is empty")
    else:
        a=str[-1]
        print("the deleted element is:",a)
        str.pop()
        if not str:
            print("stack is empty")
        else:
            print(str)
str=[]
while True:
    print("enter your option 1.push 2.pop 3.exit")
    ch=int(input())
    if(ch==1):
        push_element()
    elif(ch==2):
        pop_element()
    elif(ch==3):
        exit(0)
    else:
        print("enter the right option:")