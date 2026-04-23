class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class ll:
    def __init__(self):
        self.head=None
    
    def insertlast(self,val):
        if self.head is None:
            self.head=Node(val)
            return
        curr=self.head
        while curr.next is not None:
            curr=curr.next
        curr.next=Node(val)
    
    def display(self):
        if self.head is None:
            print("LL is Empty")
            return
        curr=self.head
        while curr :
            print("->",curr.val,end=" ")
            curr=curr.next
    
    def insertfirst(self,val):
        if self.head is None:
            self.head=Node(val)
            return
        temp=Node(val)
        temp.next=self.head
        self.head=temp
        
    def insertMiddle(self,val):
        
        if self.head is None:
            self.head=Node(val)
            return
        if self.head.next is None:
            self.head.next = Node(val)
            return
        slow=self.head
        fast=self.head

        while fast.next and fast.next.next:
            fast=fast.next.next
            slow=slow.next
        newnode = Node(val)
        newnode.next = slow.next
        slow.next = newnode
    
    def search(self,val):
        if self.head is None:
            print(val,"Not Found")
            return
        curr=self.head
        while curr is not None:
            if curr.val==val:
                print("Found")
                return
            curr=curr.next
        print(val,"Not Found")
    
    def delete(self,val):
        if self.head is None:
            print(val,"Not Found")
            return
        if val==self.head.val:
            self.head=self.head.next
            return
        curr=self.head
        while curr.next is not None:
            if curr.next.val==val:
                if curr.next.next is None:
                    curr.next=None
                else:
                    curr.next=curr.next.next
                return
            curr=curr.next
        print(val, "Not Found")
    
    def reverselinked(self):
        stack=[]
        curr=self.head
        
        while curr:
            stack.append(curr)
            curr=curr.next
        newhead=stack.pop()
        prev=newhead
        while stack:
            node=stack.pop()
            prev.next=node
            prev=node
        prev.next=None
        self.head=newhead
        
        
        
                
            
            
            
            
            
            
    
        
        
l = ll()

# 🔹 insert values

l.insertlast(10)
l.insertlast(20)
l.insertlast(30)
l.insertlast(40)
l.insertfirst(0)
l.insertMiddle(25)
l.reverselinked()


# 🔹 print list
l.display()
            
        
        