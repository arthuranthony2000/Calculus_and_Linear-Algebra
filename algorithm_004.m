clc
clear

% QUESTÃO 3

A = diag(linspace(4,4,8)) + diag(mod((1:7),  -2),1) + diag(linspace(-1,-1,6),2);
A += diag(mod((1:7),  -2),-1) + diag(linspace(-1,-1,6),-2)

b = [5 15 0 10 0 10 20 30]';

% A
fprintf("\n\n\n","")
fprintf("%s\n","A)")

[L U] = lu(A);

norm(L*U-A)

% B
fprintf("\n\n\n","")
fprintf("%s\n","B)")

y = inv(L) * b;
x1 = inv(U) * y


% C
fprintf("\n\n\n","")
fprintf("%s\n","C)")

x2 = inv(A) * b



norm(x1-x2)