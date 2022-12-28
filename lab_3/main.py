from pyDatalog import pyDatalog
from random import randrange

pyDatalog.create_terms('X,Z,N,Sum,Average,SumRnd,result')

N = 888888
Sum[X] = ((1 + X) * X) / 2
print(Sum[N] == Sum)
Average[X] = (X + 1) / 2
print(Average[N] == Average)

random_numbers = [randrange(1, N) for _ in range(100)]
random_numbers.sort()
(result["SumRnd"] == sum_(Z, for_each=Z)) <= (Z.in_(random_numbers))
print(result["SumRnd"] == SumRnd)
print("Mediana:", (random_numbers[49]+random_numbers[50])/2)
