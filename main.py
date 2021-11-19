import timeit

def print_hello():
  for i in range(1,1_000_000):
    print("test")

time = timeit.timeit(print_hello, number=1)
print(time)