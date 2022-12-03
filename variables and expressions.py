myint = 5
myfloat = 6.6
mystr = "this is anket"
mybool = True
mylist = [0,1,"two",3.4,False]
mytuple  =  (0,1,3)
mydict = {"one" : 1,"two" : 2}
print(mylist)
print(mybool)
print(mytuple)
print(mydict)
print(myint)
print(mystr)
print(myfloat)

#re-declaring a variable works
myint = "abc"
print(myint)

#to access a member of a sequence tye ,use []
print(mylist[2])
print(mytuple[1])
# use slices to get parts of a sequence
print(mylist[1:5])
print(mylist[1:5:2]) #[start:end:space]
# you can use slices to reverse a sequence
print(mylist[::-1])
# dictionaries are accessed via keys
print(mydict["one"])
#ERROR: variables of different types connot be combined
print("string type" + str(123))#str is inbulid funtion
#Global vs. local variables in functions
def somefuntion():
    global mystr                  #here i am asinging mystrasa global
    mystr  = "def"                #thos mystr id diffrent from above one
    print(mystr)
somefuntion()                      #calling funtion
print(mystr)
del mystr                          #deleting mystr  or undifing variable in realtime
print(mystr)                        #and now printing which will give error
