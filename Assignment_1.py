############################################################################
# Q2

print(5**9)
print(3//2)
print(7//3)
print(7/3)
print(6 == 6)
a = 20; a+= 30; a%=3; print(a)
print(True * False)
print(True & False)
print(True and False)
print(((6>3) and (7<4) or (18==3)) and (9>3))
print(True is False)
print(((True == False) or (False > True)) and (False <= True))


###########################################################################
#Q3

Method-1
s1= 'Nice to have it'
s2= 'here'
s3=' '.join([s1,s2])
print(s3)
#Method-2
s4= s1+' '+s2
print(s4)



########################################################################
#Q4

a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2][0])



########################################################################
#Q5


s1 = 'Nice to have it'
s2 = 'here'
a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
a.insert(0,s1)
a.append(s2)
print(a)


######################################################################
#Q6

#Method-1
 color_list_1 = set(["White", "Black", "Red"])
 color_list_2 = set(["Red", "Green"])
 print(color_list_1.difference(color_list_2))

#Method-2
print(color_list_1 - color_list_2)


####################################################################
#Q7

import string
def ispangram (str):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False
        return True

string= input('Enter Words:')
if(ispangram(string)== True):
    print('Yes')
else:
    print('No')

####################################################################
#Q8

#Method-1
n = input('input no: ')
e = '{0}+{0}{0}+{0}{0}{0}'.format(n)
f=eval(e)
print(e)
print(f)

#Method-2
a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)


##################################################################
#Q9

a = input("Input words: ")

b =a.split(",")
b.sort()
print((', ').join(b))


#################################################################
#Q10
d = {'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'],'Marks': [57,87,67,79]}
print(d['Student'][d['Marks'].index(max(d['Marks']))])

########################################################################################