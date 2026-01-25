# Markdown
## Subtitulo 1
### Subtitulo 2
* **Documentación en Github**
* Ecuaciones!
    * En Notebook de python
* Viñeta 1
* Viñeta 2
# Documentar en lenguaje de *programación*
``` python
def suma(x1:int, x2:int):
    return x1 + x2
```

``` matlab
function y = suma(x1, x2)
    y = x1+ x2;
```
# Micelánea
* Cambia distribución de teclado
windows + spacio

# Redacción de ecuaciones en Markdown 
Comando para previsualizar: ctrl+shift+v

# Ejemplo
Fórmula para calcular las raices de la ecuación cuadrática. 

$x_{1,2}= \frac{-b + \sqrt{b^2 -4ac}}{2a} $

$x_1= \frac{-b + \sqrt{b^2 -4ac}}{2a} $

$x_2= \frac{-b - \sqrt{b^2 -4ac}}{2a} $

$\pi,\alpha,\beta, \hat{y}, \leftarrow$

# Ejercicio
Escribir la ecuación Navier Stokes.
$$
\rho \frac{D\vec{v}}{Dt}
= -\,\nabla p \;+\; \mu \nabla^{2}\vec{v}
\;+\; \big(\mu_b + \tfrac{1}{3}\mu\big)\,\nabla(\nabla\!\cdot\!\vec{v})
\;+\; \rho\,\vec{f}
$$

Hay que subirlo al taller.

---

### Sumatoria
$\sum_i^4$

-----


# Taller!
* Se debe presentar:
    * Notebook
    * Enlace al repositorio

## Ejercicio 1
La sumatoria $1 + 1/2 + 1/4 +1/8 ... $ tal que el error absoluto $e_{abs} < 10^{-1}$.

``` python
#Cual es el numero minimo de elemtnos de la serie 1 + 1/2 + 1/4 + 1/8 + ...
# para alcanzar un error absoluto dentro de 10^-1?
error = 10**-1
suma = 0
n = 0
while abs(2 - suma) > error:
    suma += 1/(2**n)
    n += 1
print(n)

```


---
## Ejercicio 2 (Bubble sort)
![XSDF](.\sort.png)

### Corrida de escritorio
$v_1=[3, 2, 5, 8, 4, 1]$

| i | Vector |
| -- | -- |
| 0 | $ [3, 2, 5, 8, 4, 1] $ |
| 1 | $ [3, 2, 5, 4, 1, 8] $|
| 2 | $ [3, 2, 4, 1, 5, 8] $|
| 3 | $ [3, 2, 1, 4, 5, 8] $|
...

Resultado final:

$v_{sorted} = [1,2,3,4,5,8]$

Casos de prueba:
* $v_2=[-1, 0, 4, 5, 6, 7]$
* $v_3$ 100_000 número aleatorios entre -200 y 145. 

``` python
# Bubble Sort 
def bubble_sort(a):
    n = len(a)
    print("i | Vector")
    print("--|----------------")

    for i in range(n):
        swapped = False
        for j in range(1, n - i):
            if a[j] < a[j - 1]:
                
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
      
```
## Modifique el Algoritmo 
Determine el número de comparaciones realizadas al ordenar la serie 5, 4, 3, 2, 1

R = 10

``` python

```

---

# Algoritmo 3
![XSDF](.\fibo.png)

| n | fib(n) |
| -- | -- |
| 0 | 0 |
| 1 | 1 |
| 2 | 1 |
| 3 | 2 |
| 4 | 3 |
| 5 | 5 |
| 6 | 8 |
| 6 | 13 |
| ... | ... |
|$n = 11 $ | ? |
|$n = 84 $ | ? |
|$n = 1531$ | ? |

``` python
#fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    x,y = 0,1
    for i in range(1, n):
        z = x + y
        x, y = y, z
    return y

#Prueba de escritorio

print("Fibonacci 11 : ", fibonacci(11))
print("Fibonacci 84 : ", fibonacci(84))
print("Fibonacci 1531 : ", fibonacci(1531))

```

## Graficar!
* El valor de la serie $fib(n)$
* El valor del cociente 

    $\phi \rightarrow \frac{fib(n)} {fib(n-1)} \approx 1.618$ número áureo.


| n | $ fib(n) /fib(n-1) $ |
| -- | -- |
| 2 | $1/1=1 $ |
| 3 | $2/1 = 2$ |
| 4 | $3/2 = 1.5$ |
| 5 | $5/3= 1.66667$ |
| 6 | $8/5= 1.6$ |
| 7 | $13/8 = 1.625 $ |
| 8 | $21/13 = 1.615 $ |
| ... | ... |
|$\infty $ | $ \frac{1 + \sqrt{5}} {2} \approx 1.618$ (número áureo) |

``` python
#Grafica de la serie de Fibonacci
import matplotlib.pyplot as plt

def fib_iterative(n):
    if n == 0:
        return 0
    x, y = 0, 1
    for i in range(1, n):
        z = x + y
        x, y = y, z
    return y

# Calcular serie y cocientes
N = 20
fibs = [fib_iterative(i) for i in range(1, N + 1)]
ratios = [fibs[i] / fibs[i - 1] for i in range(1, len(fibs))]

# Graficar
plt.plot(range(2, N + 1), ratios, marker='o')
plt.axhline(y=(1 + 5**0.5)/2, color='r', linestyle='--', label='Número áureo ≈ 1.618')
plt.xlabel('n')
plt.ylabel('fib(n)/fib(n-1)')
plt.title('Convergencia de la razón de Fibonacci al número áureo')
plt.legend()
plt.grid(True)
plt.show()
```
![XSDF](.\graf.png)

### Algoritmo 03 redondeo



# Breve revisión *git*
* Inicializar repositorio
``` bash
git init 
```
* ¿Qué significa la U?
    * No están añadidos
    * Se añaden con
    ``` bash        
    git add file1 file2... 
    ```
    * Nunca!  Añade **TODO**!
    ``` bash
    git add . 
    ```
    * git commit
    ``` bash
    git commit -m "actualización de código" 
    ```
