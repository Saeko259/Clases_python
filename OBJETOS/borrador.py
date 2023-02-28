class ABC():
    variable = 0
    
    def aumentar(self,n):
        self.variable = self.variable + n
        
a = ABC()
print(a.variable)
a.aumentar(5)
print(a.variable)
b = ABC()
print(b.variable)
