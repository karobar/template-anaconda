STEP_SIZE = 0.0001

def main():
    x = 0.0
    y = 0.0
    hAn = 0.0
    for n in range(10001):
        y += hAn
        
        print()
        print("n = ", n)
        print("x = ", x)
        print("y = ", y)
         
        hAn = STEP_SIZE * 4 / (1 + pow(x, 2))

        print("hA_n = ", hAn)
        
        x += STEP_SIZE



main()