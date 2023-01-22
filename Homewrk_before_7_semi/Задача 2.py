# Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат


for i in 0,1:
    for j in 0,1:
        for k in 0,1:
            a = not (i or j or k)
            b = not i and not j and not k
a = a == b

print(a)