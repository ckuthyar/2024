s1="This is Python exam"
s2="100"
s3=100
print(s1.isalnum())
print(s2.isalnum())
#print(s3.isalnum())   AttributeError: 'int' object has no attribute 'isalnum'
print()

s1="This is Python exam"
s2="This Is Python Exam"     #every word starts with upper case
print(s1.istitle())
print(s2.istitle())
