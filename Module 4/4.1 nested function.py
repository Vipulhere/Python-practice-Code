def outerfunction():
    print("hello i am outer funtion")
    def innerfunction():
        print("hello i am inner function")
    innerfunction()
outerfunction()

print("____________-")
def num(x):
    def num1(y):
        return x*y
    return num1
result=num(20)
print(result(2))