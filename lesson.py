import math as m
# 1
def kvadrat(a, b, c):
    # a*(x**2)+(b*x) + c == 0
    D = (b**2)-4*(a*c)
    if( D > 0):
        x1 = ((-b) + m.sqrt(D))/(2*a)
        x2 = ((-b) - m.sqrt(D))/(2*a)
        return x1, type(x1), x2, type(x2)
    if(D == 0):
        x1 = (-b)/(2 * a)
        x2 = (-b)/(2 * a)
        return x1, type(x1), x2, type(x2)
    else:
        print("Уравнение не имеет решений" + "\n")
print(kvadrat(3, 6, 3))

# 2
def krug(r):
    S=(3.1415)*(r**2)
    return S

print(krug(4))

#  3
s = "Шла Маша по шосе и сосала сушку"
print("3 символ = " + s[2] + "\n" + "Предпоследний символ = " + s[len(s)-1] + "\n")

# 4
str = "приветствую"
print(str.upper(), str.lower(), str.capitalize())

# 5
# math функция переопределена как m
# print(help(m))

# 6
m = "lol"
n = 10
k = 6.14
print(dir(m), dir(n), dir(k))