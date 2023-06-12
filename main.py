import string
f=open('Alan Mathison Turing.txt', 'r')
texto= f.read() #leemos el archivo y guardxamos esta cadena en un variable
minusculas= texto.lower()#Hacemos que todas las letras sean minusculas 
listo = minusculas.translate(str.maketrans('', '', string.punctuation))#removemos la puntuacion para solo tener letras, numeros y espacios
palabras = listo.split() #Hacemos una lista con todas las palabras
anterior = palabras[0] #Esta variable nos ayuda a tener el primer valord e nuestro siguiente ciclo
contador = dict() #Creamos un diccioanrio para almacenar la palabra y su ocurrencia
alfabeto = string.printable #El alfabeto es todos los caracteres ascii, asi ya no hay que escribir una lista de ellos
letras= dict() #Diccionario con todas las letras
for i in range (0,36): #el rango es de 37, ya que solo vamos a tener letras en minsuclas=27 y diez numeor 0-9
  letra=alfabeto[i] #la letras será esa posición del alfabeto
  letras[letra]= listo.count(letra)#Agregamos la letra y la cantidad de veces que aparace
for palabra in palabras: #Ciclo para ir palabra por palabra
  if palabra in contador: #Si la palabra ya esta en mi diccioanrio, solo sumamos 1 a su ocurrencia
    contador[palabra]+=1
  else: #De lo contrario la agregamos al diccionario
    contador[palabra]=1
  if len(palabra)> len(anterior): #Si la palabra actual es de mayor longitud que la anterior, entonces actualizamos el valro de anterior para que siempre sea la mas larga
    anterior = palabra
print (f'La palabra mas larga es {palabra} con longitud {len(palabra)}') #Mostramos al usario cual es la palabra con mayor cantidad de caracteres
palabrasacomodadas=sorted(contador.items(), key=lambda x: x[1], reverse=True) #Acomodamos nuestro diccionario de palabras para que tenga valor descendiente
letrasacomodadas=sorted(letras.items(), key=lambda x: x[1], reverse=True) #Acomodamos nuestro diccionario de letras para que tenga valor descendiente
print('El diccionario de todas las palabras y sus ocurrencias es \n')
#Imprimimos los valores de ambos diccionarios de forma limpia y facil de leer
for i in palabrasacomodadas:
  print(i)
print('\nEl diccionario de todas las letras y sus ocurrencias es \n')
for i in letrasacomodadas:
  print(i)
