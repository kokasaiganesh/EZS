class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class Sll:
    def __init__(self):
        self.head=None
    def display(self):
        temp=self.head
        print("forword direction traversal")
        while (temp!=None):
            if(temp.next==None):
                print(temp.data)
            else:
                print(temp.data,"--->",end=" ")
            temp=temp.next
    def insert_at_begin(self):
        data=input("enter the data:")
        new_node=Node(data)
        new_node.next=None
        new_node.prev=None
        temp=self.head
        if(temp==None):
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node
    def insert_at_end(self):
        data=input("enter the data:")
        new_node=Node(data)
        temp=self.head
        if(temp==None):
            self.head=new_node
        else:
            new_node.next=None
            new_node.prev=None
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=new_node
            new_node.prev=temp
    def insert_at_location(self):
        loc=int(input("enter the position:"))
        temp=self.head
        if(temp==None):
            data=input("enter the data:")
            new_node=Node(data)
            new_node.next=None
            new_node.prev=None
            self.head=new_node
        else:
            if(loc==1):
                self.insert_at_begin()
            else:
                temp=self.head
                co=1
                data=input("enter the data:")
                new_node=Node(data)
                new_node.next=None
                new_node.prev=None
                while(temp!=None and co!=loc):
                    temp1=temp
                    temp=temp.next
                    co=co+1
                if(temp==None):
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
            self.head=self.head.next
            self.head.prev=None
    def delete_at_end(self):
        temp=self.head
        if(temp==None):
            print("the list is empty")
        else:
            temp=self.head
            while(temp.next!=None):
                temp1=temp
                temp=temp.next
            print("the deleted element is:",temp.data)
            temp1.next=None
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
                while(temp!=None and co!=pos):
                    temp1=temp
                    temp=temp.next
                    co=co+1
                if(temp==None):
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
                new_node.next=None
                new_node.prev=None
                if(i==1):
                    self.head=new_node
                    temp=self.head
                    new_node.prev=None
                else:
                    temp.next=new_node
                    new_node.prev=temp
                    temp=new_node
sl=Sll()
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
