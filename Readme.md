# Uplevel

Access the values of variables in the parent scope.

## Installation

```bash
pip install uplevel
```

## Usage

Here is a short example of how to use `uplevel`:

```python
from uplevel import upvar

def fib(stop: int, step: int = 0):
    if step < 2:
        result = 0 if step == 0 else 1
    elif step <= stop:
        previous = upvar(1, 'result')  # result from previous iteration
        preprevious = upvar(2, 'result')  # and one iteration before
        result = previous + preprevious
    else:
        return upvar(1, 'result')
    return fib(stop, step + 1)

print(fib(20))
```
