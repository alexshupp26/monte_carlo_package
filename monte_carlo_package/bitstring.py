import numpy as np    
import math          

class BitString:
    """
    Simple class to implement a config of bits
    """
    def __init__(self, N):
        """Constructor

        Parameters
        ----------
        N: int
            length of BitString
        """
        self.N = N
        self.config = np.zeros(N, dtype=int) 

    def __repr__(self):
        """Converts the BitString to a String

        Parameters
        ----------
        None

        Returns
        ----------
        s : String
            String representation of the BitString
        """
        s = ""
        for i in self.config:
            s+=str(i)
        return s

    def __eq__(self, other):
        """Checks if a BitString is equal to another BitString

        Parameters
        ----------
        other : BitString
            BitString being checked 

        Returns
        ----------
        : bool
            True if the two objects are equal, false otherwise
        """
        for i in range(0,min(self.N, other.N)):
            if self.config[i] != other.config[i]:
                return False
        return True
    
    def __len__(self):
        """Gets the length of the BitString Object
        
        Paramaters
        ----------
        None

        Returns
        ----------
        self.N : int
            lenght of the BitString's associated list 
        """
        return self.N

    def on(self):
        """Counts the number of "bits" in the BitString that are "on" 

        Returns
        ----------
        num : int
            the number of "on" bits in the BitString
        """
        num = 0
        for i in range(0,self.N):
            if self.config[i] == 1:
                num += 1
        return num
                
    
    def off(self):
        """Counts the number of "bits" in the BitString that are "off" 

        Returns
        ----------
        num : int
            the number of "off" bits in the BitString
        """
        num = 0
        for i in range(0,self.N):
            if self.config[i] == 0:
                num += 1
        return num
    
    def flip_site(self,i):
        """Flips a specified bit's state

        Paramaters
        ----------
        i : int
            index of the desired bit to flip
        """
        self.config[i] = (self.config[i] + 1) % 2
    
    def int(self):
        """Converts the contents of the BitString from binary to base 10
        
        Returns
        ----------
        num : int
            Base 10 integer representation of the BitString
        """
        num = 0
        power = 0
        for i in range(self.N-1, 0, -1):
            num += self.config[i] * 2**power
            power+=1             
        return num
 

    def set_config(self, s:list[int]):
        """Sets the BitString's associated list equal to a given list
        
        Paramaters
        ----------
        s : list[int]
            List that the BitString is to be set equal to
        """
        self.config = s
            
        
    def set_int_config(self, dec:int):
        """Sets the BitString's associated list equal to the binary representation of some base 10 integer
        
        Paramaters
        ----------
        dec : int
            Int that the BitString is to be set equal to
        """
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
