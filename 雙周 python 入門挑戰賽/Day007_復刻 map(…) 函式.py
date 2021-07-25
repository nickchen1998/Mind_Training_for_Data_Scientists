def add1(n):
    for i in range(len(n)):
        n[i] += 1
    return n

def isPrime(n):
    result = []

    for i in range(len(n)):
        if n[i] == 1:
            result.append(False)
            continue
        elif n[i] == 2:
            result.append(True)
            continue
        else:
            for j in range(2, n[i]):
                if n[i] % j == 0:
                    result.append(False)
                    break
                else:
                    result.append(True)
                    break
    return result

def f(L, F):
    if F == add1:
        L = add1(L)
        return L
    else:
        L = isPrime(L)
        return L

L = [1,2,3,4,5,6]
F = add1
print(f(L, F))

L = [1,2,3,4,5,6]
F = isPrime
print(f(L, F)) 
