#!/usr/bin/env python3

from uplevel import upvar


def fib(stop: int, step: int = 0):
    if step < 2:
        result = 0 if step == 0 else 1
    elif step <= stop:
        previous = upvar(1, 'result')
        preprevious = upvar(2, 'result')
        result = previous + preprevious
    else:
        return upvar(1, 'result')
    return fib(stop, step + 1)


print(fib(20))  # prints the 20th Fibonacci number
