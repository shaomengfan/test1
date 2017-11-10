Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> tup1 = ('physics', 'chemistry',1997, 2000)
>>> tup2 = (1,2,3,4,5)
>>> tup3 = "a","b","c","d"
>>> tup1 = ()
>>> tup1 = (50,)
>>> tup1 = ('physics', 'chemistry', 1997, 2000)
>>> tup2 = (1, 2, 3, 4, 5, 6, 7 )
>>> print "tup1[0]: ",tup1[0]
tup1[0]:  physics
>>> print "tup2[1:5]: ",tup2[1:5]
tup2[1:5]:  (2, 3, 4, 5)
>>> tup1 = (12, 34.56)
>>> tup2 = ('abc', 'xyz')
>>> tup1 [0] = 100

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    tup1 [0] = 100
TypeError: 'tuple' object does not support item assignment
>>> tup1[0] = 100

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    tup1[0] = 100
TypeError: 'tuple' object does not support item assignment
>>> tup3 = tup1 + tup2
>>> print tup3
(12, 34.56, 'abc', 'xyz')
>>> tup = ('physics','chemistry',1997, 20000)
>>> print tup
('physics', 'chemistry', 1997, 20000)
>>> del tup
>>> print "After deleting tup : "
After deleting tup : 
>>> print tup

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print tup
NameError: name 'tup' is not defined
>>> len((1,2,3))
3
>>> (1,2,3) + (4,5,6)
(1, 2, 3, 4, 5, 6)
>>> ('Hi!',) * 4
('Hi!', 'Hi!', 'Hi!', 'Hi!')
>>> 3 in (1,2,3)
True
>>> for x in (1,2,3)
SyntaxError: invalid syntax
>>> for x in (1,2,3):
	print x

	
1
2
3
>>> L = ('spam', 'Spam', 'SPAM!')
>>> L[2]
'SPAM!'
>>> L[-2]
'Spam'
>>> L[1:]
('Spam', 'SPAM!')
>>> print 'abc', -4.24e93, 18+6.6j, 'xyz'
abc -4.24e+93 (18+6.6j) xyz
>>> x,y=1, 2
>>> print "Value of x,y : ",x,y
Value of x,y :  1 2
>>> cmp(tuple1,tuple2)

Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    cmp(tuple1,tuple2)
NameError: name 'tuple1' is not defined
>>> tuple1,tuple2 = (123, 'xyz'), (456, 'abc')
>>> print cmp(tuple1, tuple2)
-1
>>> print cmp(tuple2, tuple1)
1
>>> tuple3 = tuple2 + (786,)
>>> print cmp(tuple2, tuple3)
-1
>>> tuple4 = (123,'xyz')
>>> print cmp(tuple1, tuple4)
0
>>> tuple1, tuple2 = (123, 'xyz', 'zara'), (456, 'abc')
>>> print "First tuple length : ",len(tuple1)
First tuple length :  3
>>> print "Sencond tuple length : ",len(tuple2)
Sencond tuple length :  2
>>> tuple1, tuple2 = (123, 'xyz', 'zara', 'abc'), (456, 700, 200)
>>> print "Max value element : ",max(tuple1)
Max value element :  zara
>>> print "Max value element : ",max(tuple2)
Max value element :  700
>>> tuple1, tuple2 = (123, 'xyz', 'zara', 'abc'), (456, 700, 200)
>>> print "min value element : ", min(tuple1)
min value element :  123
>>> print "min value element : ", min(tuple2)
min value element :  200
>>> tuple([1,2,3,4])
(1, 2, 3, 4)
>>> tuple({1:2,3:4})
(1, 3)
>>> tuple((1,2,3,4))
(1, 2, 3, 4)
>>> aList = [123, 'xyz', 'zara', 'abc']
>>> aTuple = tuple(aList)
>>> print "Tuple elements : ", aTuple
Tuple elements :  (123, 'xyz', 'zara', 'abc')
>>> tup1 = ("a11")
>>> print tup1
a11
>>> tup1 = ("a11")
>>> print tup1
a11
>>> tup1 = ("a11",)
>>> print tup1
('a11',)
>>> 
