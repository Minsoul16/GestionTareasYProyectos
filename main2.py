from tokenize import Double

def multi (num1:Double, num2:Double, num3:Double) -> Double:
    resp = num1*num2*num3
    return resp

result = multi(23,2,8)
print(result)