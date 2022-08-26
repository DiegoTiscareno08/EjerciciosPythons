# pares=[]
# impares=[]
# for n in range(10):
#     if n % 2==0:
#         pares.append(n)
#     else:
#         impares.append(n)
# print("Numeros Pares son: ",pares,"/n Numeros Impares son: ",impares)
ListPares=[ n for n in range(10) if n % 2 == 0]
ListaImpares=[n for n in range(10,20) if n %2 ==1]
print("Impares: ",ListPares)
print("Pares: ",ListaImpares)
print(ListaImpares[-1]+ListaImpares[0])

