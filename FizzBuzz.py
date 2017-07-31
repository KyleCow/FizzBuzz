n = 0

for i in range(0,100):
    n = n + 1;
    if float(n/3).is_integer():
        if float(n/5).is_integer():
            print('FizzBuzz')
        else:
            print('Fizz')
    elif float(n/5).is_integer():
        print('Buzz')
    else:
        print(n)
