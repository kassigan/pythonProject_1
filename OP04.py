"""
def sum_range(start, end):
    return sum(range(start, end+1))

print(sum_range (1,3))
"""""

def square(side_length):
    perimeter = side_length * 4
    area = side_length * side_length
    diagonal = side_length * (2 ** 0.5)
    return perimeter, area, diagonal

result = square(3)
print(result)


"""""
def bank_deposit(a, years, interest):
     for i in range(years):
         a += a * interest #каждый год увеличиваем сумму на заданный процент и прибавляем к сумме вклада
     return a

result = bank_deposit(1200, 3, 0.04)

print(result)
#print(f" You account deposit after {years} with the interest of {interest} will be {a}")
""""""""





