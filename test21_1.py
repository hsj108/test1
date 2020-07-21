"""
seq1 = "ATGTTATAG"

for i in range(0,len(seq1),3):
    print(i,seq1[i]) #인덱싱
#print(seq1[0::3])
    print(i, i+3, seq1[i:i+3]) #슬라이싱

#27번
seq1 = "ATGTTATAG"
print(seq1)
print(seq1[::-1])
"""
#28번
"""
seq1 = "ATGTTATAG"
seq1.replace("A","T")
seq1.replace("C","G")
seq1.replace("T","A")
seq1.replace("G","C")

import sys
#방법1
def comp1(seq:str)-> str:
    comp = ""
    for s in seq:
        if s =="A":
            comp +="T"
        elif s =="C":
            comp +="G"
        elif s=="G":
            comp +="C"
        elif s=="T":
            comp +="A"
    return comp

#방법2
def comp2(seq:str)-> str:
    d_comp = {"A":"T","T":"A","C":"G","G":"C"}
    comp=""
    for s in seq:
        comp +=d_comp[s]
    return comp

if __name__=="__main__":
    if len(sys.argv) !=2:
        print(f"#usage: python {sys.argv[0]} [string]")
        sys.exit()

    seq = sys.argv[1] #ATGTTATAG
    c1 = comp1(seq)
    c2 = comp2(seq)
    print(seq)
    print(c1)
    print(c2)


#29번문제 
s='ATGTTATAG'    
print("C" in s)

#33번 문제

l=['AA','AC','AG','AT']
print(l[::-1])


#30번문제
import sys
seq1 = sys.argv[1]

for i in range(0,len(seq1),1):
  # print(seq1[i:i+2])
    if seq1[i:i+2] == "TT":
        print(i,i+2,seq1[i:i+2])
#32
s.split(",")
l=s.split(",")
l.append("CA")
l
l[::-1]


#34
l = [3,1,1,2,0,0,2,3,3]
max_val = l[0]
min_val = l[0]
for elem in l:
    if elem > max_val:
        max_val = elem
    if elem < min_val:
        min_val =elem

print(f"max:{max_val}")
print(f"min:{min_val}")

"""

l = [3,1,1,2,0,0,2,3,3]

d = {}

for elem in l:
    if elem in d:
        d[elem] += 1
    else:
        d[elem] = 1

print(d)
