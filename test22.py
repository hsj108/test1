"""
class C:
    def __init__(self):
        print("class C의 인스턴스가 생성됨")
        self.name = "ccc"
        self.age = 0
    def say_hi(self):
        print("hi")
    def add_age(self, n:int):
        self.age +=n

from Bio import SeqIO

record = SeqIO.read("059.fasta","fasta")

A = record.seq.count("A")
C = record.seq.count("C")
G = record.seq.count("G")
T = record.seq.count("T")

print(f"A: {A}")
print(f"T: {T}")
print(f"G: {G}")
print(f"C: {C}")

#피보나치 수열 
f = [0,1]
import sys

def cal (n:int)->int:
    if n==0:
        return 0
    elif n ==1:
        return 1
    else:
        return cal(n-1)+cal(n-2)
    
n = int(sys.argv[1])
print(cal(n))


#K-mer generation
import sys

a1 = ["A","C","G","T"]
a2 = ["A","C","G","T"]

n= int(sys.argv[1])

def mer(a1,a2,n):
    if n ==1:
        return a2    
    
    b = []
     
    for i in a1:
        for j in a2:
            b.append(i+j)
    return mer(a1, b, n-1)    

print(mer(a1, a2, n))
"""


