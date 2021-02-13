from sympy import *

i = 0.005

f1 = lambda x: sec(x/4)**2 # 0 -> PI       #### QUESTÃO 53 - SEÇÃO 5.5
f2 = lambda x: sin(x)/(cos(x)**2) # 0 -> PI/3       ##### QUESTÃO 59 - SEÇÃO 5.5  
f3 = lambda x: (sin(x)**5)*(cos(x)**3) # PI/2 -> 3*PI/4     #### QUESTÃO 3 - SEÇÃO 7.2 
f4 = lambda x: cos(x)**2 # 0 -> PI/2        #### QUESTÃO 7 - SEÇÃo 7.2
f5 = lambda x: sin(3*x)**4 # 0 -> PI        #### QUESTÃO 9 - SEÇÃO 7.2


# função do trapezio
# y1 imagem do ponto antecedente
# y2 imagem do ponto precedente

# função do retangulo
# y imagem de algum dos pontos do retangulo




trapezio = lambda y1, y2: ((y1 + y2) * i) / 2

retangulo = lambda y: i * y

listaTrapezio = []
listaRetangulo = []

def limit_numeric(a, b, f):                
    calculoImagem = a
    while calculoImagem < b:
        pontoAntecedente = calculoImagem
        imagem1 = f(calculoImagem)        
        calculoImagem += i        
        pontoPrecedente = calculoImagem
        imagem2 = f(calculoImagem)
        calculoTrapezio = trapezio(imagem1, imagem2)
        calculoRetangulo = retangulo(imagem1)
        listaTrapezio.append(calculoTrapezio)
        listaRetangulo.append(calculoRetangulo)

#### QUESTÃO 53 - SEÇÃO 5.5
print("QUESTÃO 53 - SEÇÃO 5.5")
limit_numeric(0, pi, f1)
print("METODO RETANGULO ", sum(listaRetangulo))
print("METODO TRAPEZIO ", sum(listaTrapezio))
listaTrapezio = []
listaRetangulo = []
print("\n\n")

##### QUESTÃO 59 - SEÇÃO 5.5
print("QUESTÃO 59 - SEÇÃO 5.5")
limit_numeric(0, pi/3, f2)
print("METODO RETANGULO ", sum(listaRetangulo))
print("METODO TRAPEZIO ", sum(listaTrapezio))
listaTrapezio = []
listaRetangulo = []
print("\n\n")


#### QUESTÃO 3 - SEÇÃO 7.2
print("QUESTÃO 3 - SEÇÃO 7.2")
limit_numeric(pi/2, (3*pi)/4, f3)
print("METODO RETANGULO ", sum(listaRetangulo))
print("METODO TRAPEZIO ", sum(listaTrapezio))
listaTrapezio = []
listaRetangulo = []
print("\n\n")

#### QUESTÃO 7 - SEÇÃO 7.2
print("QUESTÃO 7 - SEÇÃO 7.2")
limit_numeric(0, pi/2, f4)
print("METODO RETANGULO ", sum(listaRetangulo))
print("METODO TRAPEZIO ", sum(listaTrapezio))
listaTrapezio = []
listaRetangulo = []
print("\n\n")

#### QUESTÃO 9 - SEÇÃO 7.2
print("QUESTÃO 9 - SEÇÃO 7.2")
limit_numeric(0, pi, f5)
print("METODO RETANGULO ", sum(listaRetangulo))
print("METODO TRAPEZIO ", sum(listaTrapezio))
listaTrapezio = []
listaRetangulo = []
print("\n\n")





        

