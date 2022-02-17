Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10
>>> print(a)
10
>>> type(a)
<class 'int'>
>>> a
10
>>> print(type(a))
<class 'int'>
>>> b=10
>>> print b
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(b)?
>>> print(b)
10
>>> c=10.2
>>> print(c)
10.2
>>> type(c)
<class 'float'>
>>> a='1'
>>> type(c)
<class 'float'>
>>> ord('a')
97
>>> chr(97)
'a'
>>> chr(2345)
'ऩ'
>>> for i in range(2300,2500):
	print(chr(i),end=' ')

	
ࣼ ࣽ ࣾ ࣿ ऀ ँ ं ः ऄ अ आ इ ई उ ऊ ऋ ऌ ऍ ऎ ए ऐ ऑ ऒ ओ औ क ख ग घ ङ च छ ज झ ञ ट ठ ड ढ ण त थ द ध न ऩ प फ ब भ म य र ऱ ल ळ ऴ व श ष स ह ऺ ऻ ़ ऽ ा ि ी ु ू ृ ॄ ॅ ॆ े ै ॉ ॊ ो ौ ् ॎ ॏ ॐ ॑ ॒ ॓ ॔ ॕ ॖ ॗ क़ ख़ ग़ ज़ ड़ ढ़ फ़ य़ ॠ ॡ ॢ ॣ । ॥ ० १ २ ३ ४ ५ ६ ७ ८ ९ ॰ ॱ ॲ ॳ ॴ ॵ ॶ ॷ ॸ ॹ ॺ ॻ ॼ ॽ ॾ ॿ ঀ ঁ ং ঃ ঄ অ আ ই ঈ উ ঊ ঋ ঌ ঍ ঎ এ ঐ ঑ ঒ ও ঔ ক খ গ ঘ ঙ চ ছ জ ঝ ঞ ট ঠ ড ঢ ণ ত থ দ ধ ন ঩ প ফ ব ভ ম য র ঱ ল ঳ ঴ ঵ শ ষ স হ ঺ ঻ ় ঽ া ি ী ু ূ ৃ 
>>> s='harish'
>>> s
'harish'
>>> s[0]='m'
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    s[0]='m'
TypeError: 'str' object does not support item assignment
>>> s.replace('h','m')
'marism'
>>> s
'harish'
>>> 
>>> s=s.replace('h','m')
>>> s
'marism'
>>> id(s)
1612279586864
>>> s=s.replace('m','h')
>>> s
'harish'
>>> id(s)
1612239880112
>>> l=[1,2,3]
>>> id[i]
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    id[i]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> id[l]
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    id[l]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> l=[1,2,3]
>>> id(l)
1612279976576
>>> l[0]=4
>>> l
[4, 2, 3]
>>> id(l)
1612279976576
>>> '''this is my house
how are you'''
'this is my house\nhow are you'
>>> """this fsdflfksd
sfsfsfsfsfs"""
'this fsdflfksd\nsfsfsfsfsfs'
>>> a="Hello world"
>>> a[2]
'l'
>>> a[7]
'o'
>>> a[8]
'r'
>>> a[5]
' '
>>> a[-5]
'w'
>>> a[-1]
'd'
>>> a[-2]
'l'
>>> a[0]
'H'
>>> a[-0]
'H'
>>> print(a[2])
l
>>> a="Aayush bansal"
>>> a
'Aayush bansal'
>>> s[0:2]
'ha'
>>> a[0:2]
'Aa'
>>> s[7:13]
''
>>> s[7:]
''
>>> s[8:]
''
>>> a[7:13]
'bansal'
>>> a[6:]
' bansal'
>>> a[-1:-2]
''
>>> a[-2:-3]
''
>>> a[2:-1]
'yush bansa'
>>> s[::2]
'hrs'
>>> a[::2]
'Ays asl'
>>> # a[ ::2] default value is 0;####
>>> a[-1::-3]
'ln uA'
>>> a[-1:-4:-1]
'las'
>>> a[-1:-13:-1]
'lasnab hsuya'
>>> a[::-1]
'lasnab hsuyaA'
>>> c="hello world"
>>> c
'hello world'
>>> c[::-1]
'dlrow olleh'
>>> print(c[::-1])
dlrow olleh
>>> a="good"
>>> a*3
'goodgoodgood'
>>> a="aayush"
>>> b="bansal"
>>> a*b
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    a*b
TypeError: can't multiply sequence by non-int of type 'str'
>>> a*a
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    a*a
TypeError: can't multiply sequence by non-int of type 'str'
>>> a*2
'aayushaayush'
>>> a+b
'aayushbansal'
>>> print('aayush bansal is genius/
      
SyntaxError: EOL while scanning string literal
>>> print('aayush bansal is genius\
nptuk)
      
SyntaxError: EOL while scanning string literal
>>> print('sfsjfsfjsd\
sffsdfd')
sfsjfsfjsdsffsdfd
>>> print('''aayush
gfnhgfj''')
aayush
gfnhgfj
>>> s
'harish'
>>> s.
SyntaxError: invalid syntax
>>> s
'harish'
>>> s
'harish'
>>> a='sdfsdfsfsf'
>>> a.format
<built-in method format of str object at 0x00000177635C2330>
>>> s
'harish'
>>> print("aaysuh bansal",.capitalize())
SyntaxError: invalid syntax
>>> print("aayush".capitalize())
Aayush
>>> k=[]
>>> type(k)
<class 'list'>
>>> k=[1,2,3,4,ausi]
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    k=[1,2,3,4,ausi]
NameError: name 'ausi' is not defined
>>> k=[1,2,3,4,5,6]
>>> type(k)
<class 'list'>
>>> k=[1,2,'hello',3+5j]
>>> k[2][3:]
'lo'
>>> ls=['apple','banana','cherry']
>>> del a[2]
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    del a[2]
TypeError: 'str' object doesn't support item deletion
>>> a
'sdfsdfsfsf'
>>> ls
['apple', 'banana', 'cherry']
>>> del ls[2]
>>> ls
['apple', 'banana']
>>> k=[1,2,3]
>>> a=k
>>> a
[1, 2, 3]
>>> k[1]=4
>>> k
[1, 4, 3]
>>> ##deep copy#
>>> a=k.copy()
>>> a
[1, 4, 3]
>>> k[1]=2
>>> k
[1, 2, 3]
>>> a
[1, 4, 3]
>>> a={'name':'harish','branch':'IT'}
>>> a[name]
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    a[name]
NameError: name 'name' is not defined
>>> print(d.get('branch'))
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    print(d.get('branch'))
NameError: name 'd' is not defined
>>> d={
	"branch":"ford",
	"model":"mustard"
	}
>>> print(d.get('branch'))
ford
>>> d
{'branch': 'ford', 'model': 'mustard'}
>>> print d
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(d)?
>>> print(d)
{'branch': 'ford', 'model': 'mustard'}
>>> s=[1,2,3]
>>> s
[1, 2, 3]
>>> print(s)
[1, 2, 3]
>>> 