class A:
    def __init__(self,x=1):
        self.x=x
class der(A):
    def __init__(self,y=2):
        super().__init__()
        self.y=y
def main():
    obj=der()
    print(obj.x,obj.y)
    
main()

#Patient 