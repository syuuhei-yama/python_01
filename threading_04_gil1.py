import logging
import concurrent
import time

def loop_number(number):
    count = 0
    for _ in range(number):
        count += 1

number = 100000000
start_time = time.time()
loop_number(number)
loop_number(number)
loop_number(number)
end_time = time.time()
print(end_time - start_time)