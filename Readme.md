# Uplevel

Access the values of variables in the parent scope.

## Installation

```bash
pip install uplevel
```

## Usage

Here is a short example of how to use `uplevel`:

```python
import uplevel

x = 3

def foo():
    return uplevel.upvar(1, 'x')

print(foo()) # 3
