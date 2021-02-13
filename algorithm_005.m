% QUESTÃO 4

clear
clc

A = [5 1 2 2 0; 3 3 2 -1 -12; 8 4 4 -5 12; 2 1 1 0 -2]


%% A)
fprintf("%s\n","A)")
fprintf("%s","MATRIZ B FORMADA PELOS VETORES A1,A2 E A4:\n")
B = [A(:,1) A(:,2) A(:,4)]

fprintf("%s","MATRIZ B AMPLIADA COM O VETOR A3:\n")
Ba3 = [B A(:,3)]
fprintf("%s","MATRIZ B AMPLIADA COM O VETOR A3 ESCALONADA NA FORMA ESCALONADA REDUZIDA:\n")
rref(Ba3)

fprintf("%s","MATRIZ B AMPLIADA COM O VETOR A5:\n")
Ba5 = [B A(:,5)]
fprintf("%s","MATRIZ B AMPLIADA COM O VETOR A5 ESCALONADA NA FORMA ESCALONADA REDUZIDA:\n")
rref(Ba5)

%% B

fprintf("%s\n\n","")

fprintf("%s\n","B)")

fprintf("%s\n","MATRIZ A AMPLIADA COM O VETOR NULO:\n")
NULA = [A [0 0 0 0]']
fprintf("%s\n","MATRIZ A AMPLIADA COM O VETOR NULO NA FORMA ESCOLONADA REDUZIDA:\n")
NULA = rref(NULA)
fprintf("%s\n","REMOVENDO A ÚLTIMA LINHA ZERADA")
NULA(1:3, :)

fprintf("%s\n","X1= -0.33333 * X3 - 3.33333 * X5")
fprintf("%s\n","X2= 8.66667*X5 -  0.33333 * X3")
fprintf("%s\n","X4= 4*X5")

fprintf("%s\n","OS VETORES QUE GERAM O ESPAÇO NULO SÃO")
v1 = [-0.33333 -0.33333 1 0 0]'
v2 = [-3.3 8.6 0 4 1]'


fprintf("%s\n\n","")




%% C
fprintf("%s\n","C)")
fprintf("%s","MATRIZ A:\n")

fprintf("%s","MATRIZ A NA FORMA ESCOLONADA REDUZIDA:\n")
rref(A)