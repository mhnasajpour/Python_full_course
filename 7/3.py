rows = int(input())
for i in range(rows):
    for j in range(i+1):
        fact_i = 1
        for k in range(2, i+1):
            fact_i *= k
        fact_j = 1
        for k in range(2, j+1):
            fact_j *= k
        fact_i_minus_j = 1
        for k in range(2, i-j+1):
            fact_i_minus_j *= k
        print(fact_i // (fact_j * fact_i_minus_j), end=' ')
    print()
