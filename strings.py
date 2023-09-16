## Strings:
           # sequance of character
           # data type

# s='"python"'
# s1="python's"
 
# s2='''python's "program"'''    #docstring
# s3="""python's "program" """
 
# print(s,s1,s2,s3)

#s="python"
### indexing -- to access the specific elements on index value
# print(s[-3])

### slicing -- to access multiple elements by index value

 # print(s[2:6:1])
 # print(s[:2])

 # print(s[-4:])
 # print(s[-4::-1])
 # print(s[::-1])

# s='''python
# program'''
 
# print(s)

## Operations of strings
# s="python"
# s1="program"

# print(s+s1)      #concatination
# print(s*3)
 
# s*=3
# print(s)

# print(s>s1)
# print(s==s1)
# print('py' in s)
# print(s is s1)

               ### Methods of strings

# s="python\tprogram"

# print(s.capitalize())
# print(s.upper())
# print(s.title())
# print(s.lower())
# print(s.casefold())
# print(s.swapcase())
 
# print(s.encode())       ##convert byte(bit)

# print(s.startswith('P'))
# print(s.endswith('m'))

# print(s.center(30))
# print(s.count('p'))

# print(s)
# print(s.expandtabs(15))     ## tabs
# print(s.index('p'))
# print(s.find('p'))
# print(s.index('p',1))
# print(s.find('p',1))

# s=input("Enter multiple data")       ### convert in array
# print(s.split())


# course="python"              ##format
# s="i am in {} batch"

# print(s.format(course))

# data={"course":"python"}
# s="i am in {course} batch"

# print(s.format_map(data))

# s="python-program"
#  print(s.split())
#  print(s.split('-'))

#  l=['python','program']                ##join string
#  print(" ".join(l))

# s="python program python"                         ##replace
# print(s.replace('python','java'))


# s="Python"                                    ##check alpha true/false
# print(s.isalpha())
# print(s.isalnum())
# print(s.isnumeric())
# print(s.isdigit())
# print(s.isdecimal())
# print(s.isprintable())
# print(s.islower())
# print(s.isupper())
# print(s.istitle())


   # s="""python program
   # java
   # php
   # ccc
   # django
   # dotnet"""
   # print(s.split())
   # print(s.splitlines())                         ###line split



### string formating
#  course=input("select course")
#  s=f"you have selected {course} batch"               (1st mathods)
#  s="you have selected %s batch"%course               (2nd mathods)

#  print(s)

# s1="python program"                          ### 1st & 2nd upper
# s2=""
# print(s[0].upper()+s[1:-1].lower()+s[-1].upper())
# print(s1.split())

# for s in s1.split():
#    s2+=s[0].upper()+s[1:-1].lower()+s[-1].upper()+" "

# print(s2)

# s1="python program"
# s2=""
# for x in s1:
#    if x not in s2:
#       s2+=x
#       print(x,'=',s1.count(x))      
      