#object-oriented, everything is an object
var1 = 'this string'
type(var1) 
#this would say "str"
print(var1)
#would show: this string

var1.upper()
#this would show: 'THIS STRING'

var1.tite()
#'This String'
var1.count()
#this would be wrong. it's an error
#count() requires an error
var1.count(i)
#would show: 2
#because there are 2 i's in 'this string'

dir(var1)
#this would show all the potential methods for a string

myvar = '     Hi.How.Are.You     '
myvar.strp()
#this removes all unneeded spaces.
#would show: 'Hi.How.Are.You'

myvar.replace('.', ' ')
#this replaces all instances of the first variable with the second
#would show: Hi How Are You