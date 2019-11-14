
def call_number():
    for number in range(0,10):
        print(number)



#call_number();

def call_numer_with_limit(limit):
    for number in range(limit):
        print(number)

##call_numer_with_limit(5)

def calculatorSum(x=1, y=1):
    return x + y

result = calculatorSum(10, 5)

print("result is {0}".format(result))
