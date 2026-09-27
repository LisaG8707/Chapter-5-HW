def chaos(k, x, n):
    for i in range(n):
        x = k * x * (1 - x)
        print(x)
def main():
        k = float(input("Enter the value for k: "))
        x = float(input("Enter the starting value for x: "))
        n = int(input("Enter the number of iterations: "))
        chaos(k, x, n)
            
main()
