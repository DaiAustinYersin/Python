# Bài 5 - Kiểm tra số nguyên tố
def isPrime(n):
    if n > 1:
        for i in range(2,n+1):
            if n % i == 0:
                return False
            else:
                return True
        else:
            return False



# Bài 5 - In dãy Fibonacci
def fib(n):
    for i in range(1,n+1):
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fib(n-1) + fib(n-2)



# Bài 5 - Tính giá trị biểu thức S
# Hàm tính  S = (x^2+ 1)^n
def tinhS(x,n):
    if n == 0:
        return 1
    else:
        S = 1
        for i in range(0,n):
            S *= (x*x + 1)
        return S


# Bài 5 - Tính giá trị biểu thức A
# Hàm tính  A = (x^2 + x + 1)^n + (x^2 - x + 1)^n
def tinhA(x,n):
    if n == 0:
        return 2
    else:
        A1 = 1
        A2 = 2
        for i in range(0,n):
            A1 *= (x*x + x + 1)
            A2 *= (x*x - x + 1)
        return A1+A2




