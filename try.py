def solution(number):
    suma =0
    if number<0:
        return 0
    else:
        for n in range(0,number):
            print(n)
            if n%3==0 or n%5==0:
                print(n)
                suma=suma+n
    print(suma)

solution(10)