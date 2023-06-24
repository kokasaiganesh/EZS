class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class CDll:
    def __init__(self):
        self.head=None
    def display(self):
        temp=self.head
        print("forword direction traversal")
        if(temp==None):
            print("list is empty")
        else:
            print("forword direction:")
            while (temp.next!=self.head):
                print(temp.data,"--->",end=" ")
                temp=temp.next
            if(temp.next==self.head):
                print(temp.data)
    def insert_at_begin(self):
        data=input("enter the data:")
        new_node=Node(data)
        new_node.next=new_node
        new_node.prev=new_node
        temp=self.head
        if(temp==None):
            self.head=new_node
        else:
            while(temp.next!=self.head):
                temp=temp.next
            new_node.next=self.head
            self.head=new_node
            new_node.prev=temp
            temp.next=self.head
    def insert_at_end(self):
        data=input("enter the data:")
        new_node=Node(data)
        temp=self.head
        if(temp==None):
            self.head=new_node
        else:
            new_node.next=new_node
            new_node.prev=new_node
            temp=self.head
            while(temp.next!=self.head):
                temp=temp.next
            temp.next=new_node
            new_node.prev=temp
            new_node.next=self.head
    def insert_at_location(self):
        loc=int(input("enter the position:"))
        temp=self.head
        if(temp==None):
            data=input("enter the data:")
            new_node=Node(data)
            new_node.next=new_node
            new_node.prev=new_node
            self.head=new_node
        else:
            if(loc==1):
                self.insert_at_begin()
            else:
                temp=self.head
                co=1
                data=input("enter the data:")
                new_node=Node(data)
                new_node.next=new_node
                new_node.prev=new_node
                while(temp.next!=self.head and co!=loc):
                    temp1=temp
                    temp=temp.next
                    co=co+1
                if(temp==self.head):
                    print("The position is not found")
                    print("Plese enter the correct position")
                else:
                    temp1.next=new_node
                    new_node.prev=temp1
                    new_node.next=temp
                    temp.prev=new_node
    def delete_at_begin(self):
        temp=self.head
        if(temp==None):
            print("the linked list is empty")
        else:
            print("the deleted element is :",self.head.data)
            while(temp.next!=self.head):
                temp=temp.next
            self.head=self.head.next
            self.head.prev=temp
            temp.next=self.head
    def delete_at_end(self):
        temp=self.head
        if(temp==None):
            print("the list is empty")
        else:
            temp=self.head
            while(temp.next!=self.head):
                temp1=temp
                temp=temp.next
            print("the deleted element is:",temp.data)
            temp1.next=self.head
    def delete_at_pos(self):
        pos=int(input("enter the position:"))
        temp=self.head
        if(temp==None):
            print("the linked list ia empty")
        else:
            if(pos==1):
                self.delete_at_begin()
            else:
                temp=self.head
                co=1
                while(temp.next!=self.head and co!=pos):
                    temp1=temp
                    temp=temp.next
                    co=co+1
                if(temp==self.head):
                    print("the position is nort found")
                else:
                    te=temp.next
                    t=temp.prev
                    print("the deleted element is:",temp.data)
                    temp1.next=te
                    t.next=temp1
                    temp1.prev=t
    def creation(self):
        temp=self.head
        if(temp!=None):
            print("list is already created")
        else:
            n=int(input("enter no of nodes:"))
            for i in range(1,n+1):
                data=input("enter the data:")
                new_node=Node(data)
                new_node.next=new_node
                new_node.prev=new_node
                if(i==1):
                    self.head=new_node
                    temp=self.head
                else:
                    temp.next=new_node
                    new_node.prev=temp
                    new_node.next=self.head
                    temp=new_node
sl=CDll()
while(1):
    print("enter your option:")
    print("1.create 2.insert at begin 3.insert at end 4.insert at location 5.delete at begin 6.delete at end 7.delete at location 8.exit 9.display")
    n=int(input())
    if(n==1):
        sl.creation()
    elif(n==2):
        sl.insert_at_begin()
    elif(n==3):
        sl.insert_at_end()
    elif(n==4):
        sl.insert_at_location()
    elif(n==5):
        sl.delete_at_begin()
    elif(n==6):
        sl.delete_at_end()
    elif(n==7):
        sl.delete_at_pos()
    elif(n==8):
        exit(0)
    elif(n==9):
        sl.display()
    else:
        print("enter the correct option")

