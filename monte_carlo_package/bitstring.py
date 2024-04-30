import numpy as np    
import math          

class BitString:
    """
    Simple class to implement a config of bits
    """
    def __init__(self, N):
        self.N = N
        self.config = np.zeros(N, dtype=int) 

    def __repr__(self):
        s = ""
        for i in self.config:
            s+=str(i)
        return s

    def __eq__(self, other):
        for i in range(0,min(self.N, other.N)):
            if self.config[i] != other.config[i]:
                return False
        return True
    
    def __len__(self):
        return self.N

    def on(self):
        num = 0
        for i in range(0,self.N):
            if self.config[i] == 1:
                num += 1
        return num
                
    
    def off(self):
        num = 0
        for i in range(0,self.N):
            if self.config[i] == 0:
                num += 1
        return num
    
    def flip_site(self,i):
        self.config[i] = (self.config[i] + 1) % 2
    
    def int(self):
        num = 0
        power = 0
        for i in range(self.N-1, 0, -1):
            num += self.config[i] * 2**power
            power+=1             
        return num
 

    def set_config(self, s:list[int]):
        self.config = s
            
        
    def set_int_config(self, dec:int):
        if (dec == 0): 
            temp = 0
            while (temp < self.N):
                self.config[temp] = 0
                temp+=1
        else:
            length = 0
            temp = dec
            while (temp !=0):
                temp = int(temp/2)
                length+=1
            for i in range(self.N-1, self.N-length-1,-1):
                self.config[i] = dec%2
                dec = int(dec / 2)
