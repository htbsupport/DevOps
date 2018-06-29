#!/usr/bin/python

class MyClass:
  
   def __init__(self):
     print ("This is called as constructor")
     print ("You can initialize member variables here automatically")
     self.x = 100
     self.y = 200

  def setValues( self, val1, val2 ):
      self.x = val1
      self.y = val2

  def printvalues(self, val1, val2):
      print ("value of x is", self.x)
      print ("value of y is", self.y)
      print ("\n")

if __name__ == "__main__":
     print ("Constructing object 1")
     obj1 = MyClass()

     print ("Constructing object 2")
     obj2 = MyClass()

     print ("Before calling Setvalue function")
     print ("object 1 values")
     obj1.printValues()

    print ("Object 2 values")
    obj2.printvalues()

    print ("After calling service")
   
    obj1.setValues(500,600)
    obj2.setvalues(10,20) 

    print ("object 1 values")    
    obj1.prontvalues()

    print ("object 2 values")
    obj2.printvalues()
