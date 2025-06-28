import sys
import time


def fib(n):
    if n <= 1:
        return 1
    
    f = [0] * (n+1)
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]



def main():
    n = int(sys.argv[1])
    start = time.time()
    print(fib(n))
    end = time.time()
    print(f"For running fib({n}), time was {(end - start)* 1000} milliseconds")

if __name__ == "__main__":
    main()