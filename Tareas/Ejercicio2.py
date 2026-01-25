# Bubble Sort optimizado
def bubble_sort(a):
    n = len(a)
    print("i | Vector")
    print("--|----------------")

    for i in range(n):
        swapped = False
        for j in range(1, n - i):
            if a[j] < a[j - 1]:
                # Intercambio
                a[j], a[j - 1] = a[j - 1], a[j]
                swapped = True
        
       
        print(f"{i} | {a}")

        
        if not swapped:
            break

    return a


#Prueba de escritorio
v1 = [3, 2, 5, 8, 4, 1]
print("Vector original:", v1)
v_sorted = bubble_sort(v1.copy())
print("Resultado ordenado:", v_sorted)

#Caso de prueba
v2 = [ -1, 0, 4, 5, 6, 7]
import random
#v3 = [random.randint(-200, 145) for _ in range(100000)]

print("\n Caso 2 :",  bubble_sort(v2.copy()))
#print("\n Caso 3 (random) :", bubble_sort(v3.copy()))

      