__version__ = "0.0.5"

import inspect
import sys
import typing


def upvar(level: int, varname: str):
    try:
        return sys._getframe(level + 1).f_locals[varname]
    except ValueError:
        return ValueError(f"Level {level} not available.")
    except KeyError:
        return ValueError(f"Variable {varname} not found in the scope.")


def upset(level: int, varname: str, value: typing.Any):
    try:
        sys._getframe(level + 1).f_locals[varname] = value
    except ValueError:
        return ValueError(f"Level {level} not available.")
