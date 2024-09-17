__version__ = "0.0.2"

import sys


def upvar(level: int, varname: str):
    try:
        return sys._getframe(level).f_back.f_locals[varname]
    except ValueError:
        return ValueError(f"Level {level} not available.")
    except KeyError:
        return ValueError(f"Variable {varname} not found in the scope.")
