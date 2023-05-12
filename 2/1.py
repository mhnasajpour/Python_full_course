a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())

sum = a + b + c + d + e
prd = a * b * c * d * e
avg = sum / 5
var = ((a-avg)**2 + (b-avg)**2 + (c-avg)**2 + (d-avg)**2 + (e-avg)**2) / 5

print('SUM:', sum)
print('PRD:', prd)
print('AVG:', avg)
print('VAR:', var)
