def calcPmt(P0, r, k, N):
    d = P0 / ((1 - (1 + r / k) ** (-N * k)) / (r / k))
    return d

def main():
    P0 = float(input("Enter the amount to finance: "))
    r = float(input("Enter the annual interest rate as a decimal: "))
    k = int(input("Enter the number of times interest is compounded per year: "))
    N = int(input("Enter the number of years: "))
    payment = calcPmt(P0, r, k, N)
    print("Monthly payment: $", round(payment, 2))

main()
          
