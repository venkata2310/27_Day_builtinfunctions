'''sorted()'''
# a=[1,6,3,8,2]
# a.sort()
# print(a)
# print(sorted([12,10,14,13,8,10]))
# print(sorted((12,14,19,2,4,10,15)))

'''all()'''
# print(all([True,1,10]))
# print(all([True,1,2,'']))
# print(all([True,1,2,' ']))
# print(all([True,1,2,'  ']))
# print(all([True,1,0,'']))
# print(all([False,1,0,'']))
# print(all([True,1,2,'']))
# print(all([True,1,2,None]))
# print(all([False,1,2,None]))

'''any()'''
# print(any([True,False,False,23]))
# print(any([False,False,0]))
# print(any([True,False,None,0]))

'''bool()'''
# print(bool(False))
# print(bool(1))
# print(bool(0))
# print(bool(None))
# print(bool('bool'))

'''eval()'''
# print('eval=',eval('5+6.8-1'))
# a=eval('5+6-1')
# b=eval('4+3.8-1')
# print(a,type(a))
# print(b,type(b))

'''sum()'''
# print('sum=',sum([1,2,3,4,5]))
# print('sum=',sum((10.5,20,30)))

'''reversed()-list'''
# for i in reversed([1,2,3,4]):
#     print(i)

'''reversed()-tuple'''
# for i in reversed((10,20,30,40)):
#     print(i)

'''enumerate()'''
a=['bread','milk','python']
b=enumerate(a)
print(type(b))
print(dict(b))
print(list(b))
print(tuple(b))

a=['bread','milk','python']
c=enumerate(a,6)
print(list(c))