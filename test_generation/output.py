'''
Created on 15-10-2013

@author: Chun Trang
'''

from input import main
import random
import re
import itertools
import unittest

xau = []
list1 = []
list_left = []
list_right = []
r_list = []
check = 0

# Sap xep noi bot
def sort_list(a,b):
    for i in range(len(a)-1):
        for j in range(0, len(a)-1):
            if (a[j] >= a[j+1]):
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                temp = b[j]
                b[j] = b[j+1]
                b[j+1] = temp
#Kiem tra su chong cheo
def check_list(a,b):
    for i in range(1, len(a)):
            if (a[i] <= b[i-1]):
                raise Exception ("Error")

# Lay random trong list
def random_list(L1,L2):
    r_list = L1
    for i in range(len(L1)):
        for j in range(len(L1[i])):
            r_list[i][j]= random.randint(L1[i][j], L2[i][j])
    return r_list
    
# Lay comment
with open("Input.py") as f:
    for line in f:
        if "'''" in line:
            if check == 0:
                check = 1
                continue
        if "'''" in line:
            if check == 1:
                check = 0              
        if check == 1:
            xau.append(line)

#Chi lay ra cac so, ke ca so am
for i in range(len(xau)):
    xau[i] = re.findall(r'[-0-9]+', xau[i]) 
print xau

j = 0
for i in range(len(xau)):
    lf = []
    lr = []
    for j in range(len(xau[i])):
        if (j%2 == 0):
            lf.append(xau[i][j])    # Cac phan tu o vi tri le thuoc list_left, phai thuoc list_right
        else: 
            lr.append(xau[i][j])
    list_left.append(lf)
    list_right.append(lr)
#print list_left
#print list_right
#print "\n"
for i in range(len(list_right)):
    for j in range(len(list_right[i])):
        list_right[i][j] = int(list_right[i][j])    #Covert ve kieu int
        list_left[i][j] = int(list_left[i][j])
        
#sap xep
for i in range(len(list_left)):
    sort_list(list_left[i],list_right[i])
    
# In thu ra cac mang dc phan tach   
print list_left
print list_right

#Kiem tra su chong cheo tham so dau vao
for i in range(len(list_left)):
    check_list(list_left[i],list_right[i])
    
#In ra xau trc khi test
print xau

a = random_list(list_left,list_right)
xau = list(itertools.product(*a))

# Print ra xau chua cac testcase
print xau
print "A number of testcase: " 
print len(xau)

class Test(unittest.TestCase):
    pass

def test_main(a):
    def test(self):
        self.assertAlmostEqual(0,main(*a))
    return test

if __name__ == "__main__":
    j = 0
    for i in xau:
        testName = "test_Name" + str(j)
        j = j+1
        test = test_main(i)
        setattr(Test,testName,test)
    unittest.main()
        