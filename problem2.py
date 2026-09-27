def kToF(k):
    f = (k - 273.15) * 9 / 5 + 32
    return f

def main():
    print("Kelvin\tFahrenheit")
    for k in range(0, 301, 20):
        f = kToF(k)
        print(k, "\t", f)

main()

        
