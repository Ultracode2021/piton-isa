Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
lista=[ "fresa", "uva", "sandia", "piña"]

print(len(lista))
4
for elemento in lista:
    print(elemento)

    
fresa
uva
sandia
piña
listaDos=["Juan", "Pedro", 25]
listaEfe=lista+listaDos
print(listaEfe)
['fresa', 'uva', 'sandia', 'piña', 'Juan', 'Pedro', 25]
if 25 in listaDos
SyntaxError: expected ':'
if 25 in listDos:
    print("Si")
else:
    print("No")

    
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    if 25 in listDos:
NameError: name 'listDos' is not defined. Did you mean: 'listaDos'?


=============== RESTART: /Volumes/AQUARIUS/Python/Basic/diqui.py ===============
Traceback (most recent call last):
  File "/Volumes/AQUARIUS/Python/Basic/diqui.py", line 3, in <module>
    print(diccionario[Kathy])
NameError: name 'Kathy' is not defined

=============== RESTART: /Volumes/AQUARIUS/Python/Basic/diqui.py ===============
26

=============== RESTART: /Volumes/AQUARIUS/Python/Basic/diqui.py ===============
26
4

=============== RESTART: /Volumes/AQUARIUS/Python/Basic/diqui.py ===============
26
4
Traceback (most recent call last):
  File "/Volumes/AQUARIUS/Python/Basic/diqui.py", line 6, in <module>
    conjunto=diccionario[2:3]
TypeError: unhashable type: 'slice'

=============== RESTART: /Volumes/AQUARIUS/Python/Basic/diqui.py ===============
26
4
Traceback (most recent call last):
  File "/Volumes/AQUARIUS/Python/Basic/diqui.py", line 6, in <module>
    conjunto=diccionario[2:3]
TypeError: unhashable type: 'slice'

=============== RESTART: /Volumes/AQUARIUS/Python/Basic/diqui.py ===============
26
4
Traceback (most recent call last):
  File "/Volumes/AQUARIUS/Python/Basic/diqui.py", line 6, in <module>
    conjunto=diccionario[:3]
TypeError: unhashable type: 'slice'

=============== RESTART: /Volumes/AQUARIUS/Python/Basic/diqui.py ===============
26
4
Traceback (most recent call last):
  File "/Volumes/AQUARIUS/Python/Basic/diqui.py", line 6, in <module>
    conjunto=diccionario[0:3]
TypeError: unhashable type: 'slice'

=============== RESTART: /Volumes/AQUARIUS/Python/Basic/diqui.py ===============
26
4
('Uva', 'Fresa', 'Kiwi')

=============== RESTART: /Volumes/AQUARIUS/Python/Basic/diqui.py ===============
26
4
('Uva', 'Fresa', 'Kiwi')

=============== RESTART: /Volumes/AQUARIUS/Python/Basic/diqui.py ===============
26
4
('Kiwi', 'Piña')

=============== RESTART: /Volumes/AQUARIUS/Python/Basic/diqui.py ===============
26
4
Traceback (most recent call last):
  File "/Volumes/AQUARIUS/Python/Basic/diqui.py", line 7, in <module>
    conjunto=frutas[1,2]
TypeError: tuple indices must be integers or slices, not tuple

=============== RESTART: /Volumes/AQUARIUS/Python/Basic/diqui.py ===============
26
4
('Kiwi', 'Piña', 'Melón')

================ RESTART: /Volumes/AQUARIUS/Python/Basic/proj.py ===============
Help on tuple object:

class tuple(object)
 |  tuple(iterable=(), /)
 |  
 |  Built-in immutable sequence.
 |  
 |  If no argument is given, the constructor returns an empty tuple.
 |  If iterable is specified the tuple is initialized from iterable's items.
 |  
 |  If the argument is a tuple, the return value is the same object.
 |  
 |  Built-in subclasses:
 |      asyncgen_hooks
 |      UnraisableHookArgs
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __getnewargs__(self, /)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  __class_getitem__(...) from builtins.type
 |      See PEP 585
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.


================ RESTART: /Volumes/AQUARIUS/Python/Basic/proj.py ===============


================ RESTART: /Volumes/AQUARIUS/Python/Basic/proj.py ===============

type[1]

================ RESTART: /Volumes/AQUARIUS/Python/Basic/proj.py ===============

type[1, 2, 3, 4, 5, 6]

================ RESTART: /Volumes/AQUARIUS/Python/Basic/proj.py ===============

<class 'tuple'>

================ RESTART: /Volumes/AQUARIUS/Python/Basic/proj.py ===============

<class 'tuple'>
6

================ RESTART: /Volumes/AQUARIUS/Python/Basic/proj.py ===============

<class 'tuple'>
6
24

================ RESTART: /Volumes/AQUARIUS/Python/Basic/proj.py ===============

<class 'tuple'>
6
24
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']

============== RESTART: /Volumes/AQUARIUS/Python/Basic/objetis.py ==============


============== RESTART: /Volumes/AQUARIUS/Python/Basic/objetis.py ==============
<class '__main__.Galeria'>

============== RESTART: /Volumes/AQUARIUS/Python/Basic/objetis.py ==============
<class 'type'>

============== RESTART: /Volumes/AQUARIUS/Python/Basic/objetis.py ==============
Traceback (most recent call last):
  File "/Volumes/AQUARIUS/Python/Basic/objetis.py", line 17, in <module>
    print(len(Galeria))
TypeError: object of type 'type' has no len()

============== RESTART: /Volumes/AQUARIUS/Python/Basic/objetis.py ==============
Traceback (most recent call last):
  File "/Volumes/AQUARIUS/Python/Basic/objetis.py", line 29, in <module>
    print(len(Galeria))
TypeError: object of type 'type' has no len()

============== RESTART: /Volumes/AQUARIUS/Python/Basic/objetis.py ==============


============== RESTART: /Volumes/AQUARIUS/Python/Basic/objetis.py ==============
0

============== RESTART: /Volumes/AQUARIUS/Python/Basic/objetis.py ==============
5

=============== RESTART: /Volumes/AQUARIUS/Python/Basic/fixie.py ===============
Traceback (most recent call last):
  File "/Volumes/AQUARIUS/Python/Basic/fixie.py", line 5, in <module>
    crearArchivos()
NameError: name 'crearArchivos' is not defined

=============== RESTART: /Volumes/AQUARIUS/Python/Basic/fixie.py ===============
Traceback (most recent call last):
  File "/Volumes/AQUARIUS/Python/Basic/fixie.py", line 13, in <module>
    crearFixie()
  File "/Volumes/AQUARIUS/Python/Basic/fixie.py", line 2, in crearFixie
    fix=open("merti.txt", "escritura")
ValueError: invalid mode: 'escritura'

=============== RESTART: /Volumes/AQUARIUS/Python/Basic/fixie.py ===============
Traceback (most recent call last):
  File "/Volumes/AQUARIUS/Python/Basic/fixie.py", line 13, in <module>
    crearFixie()
  File "/Volumes/AQUARIUS/Python/Basic/fixie.py", line 2, in crearFixie
    fix=open("merti.txt", "escritura")
ValueError: invalid mode: 'escritura'

=============== RESTART: /Volumes/AQUARIUS/Python/Basic/fixie.py ===============
Traceback (most recent call last):
  File "/Volumes/AQUARIUS/Python/Basic/fixie.py", line 13, in <module>
    crearFixie()
  File "/Volumes/AQUARIUS/Python/Basic/fixie.py", line 2, in crearFixie
    fix=open("merti.txt", "e")
ValueError: invalid mode: 'e'

=============== RESTART: /Volumes/AQUARIUS/Python/Basic/fixie.py ===============
Traceback (most recent call last):
  File "/Volumes/AQUARIUS/Python/Basic/fixie.py", line 13, in <module>
    crearFixie()
  File "/Volumes/AQUARIUS/Python/Basic/fixie.py", line 2, in crearFixie
    fix=open("merti.txt", "e")
ValueError: invalid mode: 'e'

=============== RESTART: /Volumes/AQUARIUS/Python/Basic/fixie.py ===============

=============== RESTART: /Volumes/AQUARIUS/Python/Basic/fixie.py ===============


=============== RESTART: /Volumes/AQUARIUS/Python/Basic/fixie.py ===============

=============== RESTART: /Volumes/AQUARIUS/Python/Basic/fixie.py ===============

=============== RESTART: /Volumes/AQUARIUS/Python/Basic/fixie.py ===============

=============== RESTART: /Volumes/AQUARIUS/Python/Basic/fixie.py ===============
Traceback (most recent call last):
  File "/Volumes/AQUARIUS/Python/Basic/fixie.py", line 23, in <module>
    leerDram()
  File "/Volumes/AQUARIUS/Python/Basic/fixie.py", line 12, in leerDram
    rain.open("fax.txt","r")
NameError: name 'rain' is not defined

=============== RESTART: /Volumes/AQUARIUS/Python/Basic/fixie.py ===============
Traceback (most recent call last):
  File "/Volumes/AQUARIUS/Python/Basic/fixie.py", line 20, in <module>
    leerDram()
  File "/Volumes/AQUARIUS/Python/Basic/fixie.py", line 12, in leerDram
    rain.open("fax.txt","r")
NameError: name 'rain' is not defined

=============== RESTART: /Volumes/AQUARIUS/Python/Basic/fixie.py ===============
Traceback (most recent call last):
  File "/Volumes/AQUARIUS/Python/Basic/fixie.py", line 20, in <module>
    leerDram()
  File "/Volumes/AQUARIUS/Python/Basic/fixie.py", line 12, in leerDram
    rain.open("fax.txt","r")
NameError: name 'rain' is not defined

=============== RESTART: /Volumes/AQUARIUS/Python/Basic/fixie.py ===============
Traceback (most recent call last):
  File "/Volumes/AQUARIUS/Python/Basic/fixie.py", line 20, in <module>
    leerDram()
  File "/Volumes/AQUARIUS/Python/Basic/fixie.py", line 12, in leerDram
    rix.open("fax.txt","r")
NameError: name 'rix' is not defined

=============== RESTART: /Volumes/AQUARIUS/Python/Basic/fixie.py ===============
Traceback (most recent call last):
  File "/Volumes/AQUARIUS/Python/Basic/fixie.py", line 20, in <module>
    leerDram()
  File "/Volumes/AQUARIUS/Python/Basic/fixie.py", line 12, in leerDram
    fix.open("fax.txt","r")
NameError: name 'fix' is not defined

=============== RESTART: /Volumes/AQUARIUS/Python/Basic/fixie.py ===============
Traceback (most recent call last):
  File "/Volumes/AQUARIUS/Python/Basic/fixie.py", line 21, in <module>
    leerDram()
  File "/Volumes/AQUARIUS/Python/Basic/fixie.py", line 12, in leerDram
    fix.open("fax.txt","r")
NameError: name 'fix' is not defined

=============== RESTART: /Volumes/AQUARIUS/Python/Basic/fixie.py ===============
Mis conocimientos

Intro
