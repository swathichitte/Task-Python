class A:
    def method_a(self):
        print("This is from class A")
 
class Parent(A):
    def method_parent(self):
        print("This is from class Parent")
 
class Child(Parent):
    def method_child(self):
        print("This is from class Child")
 
obj = Child()
 
obj.method_a()  
obj.method_parent()    
obj.method_child()    
