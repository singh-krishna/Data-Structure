# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 21:09:11 2019

@author: HP
"""

"""
Single Linked List program where we have a node which are divided into two part |info/link|
info stores the data,data may be any type integer,character,string etc
link stores the address of the next node
OPERATION THAT CAN BE IMPLEMENTED:-
insertion(begning,end,speacific node)
deletion(begning,end,speacific node)
searching
number of nodes
"""
class Node:
     def __init__(self,value):
         self.info=value
         self.link=None
class Single_linked_list:
    def __init__(self):
        self.start=None
    def insert_at_begning(self,data):
        temp=Node(data)
        temp.link=self.start
        self.start=temp
    def Display(self):
        if self.start is None:
            print("List is empty")
        else:
            print("List is:-")
            p=self.start
            while p is not None:
                print(p.info,"-->",end='')
                p=p.link
    def Number_of_node(self):
        if self.start is None:
            print("List is empty")
        else:
            x=0
            p=self.start
            while p is not None:
                x +=1
                p=p.link
            print("Number of nodes:-%d" %x)
    def Delete(self,val):
        p=self.start
        for x in range(val-1):
            p=p.link
        p.link=p.link.link
    def Search(self):
            val=int(input("enter the number to be searched"))
            self.val=val
            p=self.start
            self.count1 = 0
            while p is not None:
                if self.val == p.info:
                    self.count1 +=1
                p=p.link
            if self.count1 > 0:
                print("value is present %d" %val)
                print("number of time present %d" %self.count1)
            else:
                print("value is not present %d" %self.val)
    def insert_at_particular_node(self,place):
        p=self.start
        for x in range(0,place):
            
            p=p.link
        data=int(input("enter number"))
        temp=Node(data)
        temp.link=p.link
        p.link=temp
    def insert_at_end1(self):
        n=int(input("enter number of node:-"))
        for x in range(0,n):
            data=int(input("enter number:-"))
            temp=Node(data)
            if self.start is None:
                self.start=temp
            else:
                p=self.start
                while p.link is not None:
                    p=p.link
                p.link=temp 
    def maximum_value(self):
        max=0
        p=self.start
        while p is not None:
            if(p.info>max):
                max=p.info
            else:
                p=p.link
        print("maximum value is %d" %max)
obj=Single_linked_list()
x=1
while x == 1:
    print("\n1.Insert at begning\n2.Display\n3.Number of node\n4.Search\n5.exit\n6.Insert at end\n7.Insert at particular node\n8.Delete node\n9.Maximum value\n")
    choice=int(input("enter your choice:--"))
    if choice == 1:
        var=int(input("enter number:-"))
        obj.insert_at_begning(var)
    elif choice== 2:
        obj.Display()
    elif choice== 3:
        obj.Number_of_node()
    elif choice== 4:
        obj.Search()
    elif choice== 5:
        break
    elif choice== 6:
            obj.insert_at_end1()
    elif choice== 7:
        var=int(input("enter node where you have to insert:-"))
        obj.insert_at_particular_node(var)
    elif choice== 8:
        no=int(input("enter node number to delete:-"))
        obj.Delete(no)
    elif choice== 9:
        obj.maximum_value()
    else:
        print("wrong choice\n")
    
    
    
    
    
    
    
    