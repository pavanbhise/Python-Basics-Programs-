class Ram:
          def __init__(self,name,age):
              self.name=name
              self.age = age
try:
    a=input('enter name')
    b=int(input('enter age'))
    p= Ram( a,b)
    x=print(p.name,p.age)
except:
        print('somthing went wrong')
        