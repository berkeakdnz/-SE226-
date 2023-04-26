def sieveOfEratosthenesFunc(arr):
    primes = [0] * 100
    numPrimes = 0

    for i in range(len(arr)):
        num = arr[i]
        isPrime = True

        if num <= 1:
            isPrime = False
        else:
            for j in range(2, int(num ** 0.5) + 1):
                if num % j == 0:
                    isPrime = False
                    break

        if isPrime:
            primes[numPrimes] = num
            numPrimes += 1

    for i in range(len(primes)):
        if primes[i] != 0 and primes[i] != -1:
            currPrime = primes[i]
            numPrimes -= 1

            for j in range(i + 1, len(primes)):
                if primes[j] != 0 and primes[j] != -1 and primes[j] % currPrime == 0:
                    primes[j] = -1

    result = [0] * (numPrimes + 1)
    index = 0

    for i in range(len(primes)):
        if primes[i] != 0 and primes[i] != -1:
            result[index] = primes[i]
            index += 1

    result[index] = 0
    return result