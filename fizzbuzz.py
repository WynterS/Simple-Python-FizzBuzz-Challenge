currentNumber = 1
fizzNum = 0
buzzNum = 0
fizzBuzzNum = 0

while currentNumber <= 1000:
    if currentNumber % 3 == 0 and currentNumber % 5 == 0:
        print('fizzbuzz')
        fizzBuzzNum += 1
    elif currentNumber % 3 == 0:
        print('fizz')
        fizzNum += 1
    elif currentNumber % 5 == 0:
        print('buzz')
        buzzNum += 1
    else:
        print(currentNumber)
    currentNumber += 1

print('-----------------------')
print('Said Fizz %s times' % (fizzNum))
print('Said Buzz %s times' % (buzzNum))
print('Said FizzBuzz %s times' % (fizzBuzzNum))
