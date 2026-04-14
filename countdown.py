from time import sleep

def countdown(n):
    while n>=0:
        print(n)
        sleep(1)
        n -= 1

def countdown_recursive(n):
    #condizione terminale
    if n == 0:
        print("stop")
    else:
        sleep(1)
        print(n)
        countdown_recursive(n-1)


if __name__=="__main__":
    n=10
    countdown_recursive(n)
