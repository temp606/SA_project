"""Simple calculator application.

Provides basic operations: add, subtract, multiply, divide.
Can be used as a module or from the command line.
"""

import argparse
import sys


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def main():
    parser = argparse.ArgumentParser(description="Simple calculator CLI")
    parser.add_argument("x", type=float, help="First operand")
    parser.add_argument("y", type=float, help="Second operand")
    parser.add_argument(
        "operation",
        choices=["add", "sub", "mul", "div"],
        help="Operation to perform: add, sub, mul, div",
    )
    args = parser.parse_args()

    ops = {
        "add": add,
        "sub": subtract,
        "mul": multiply,
        "div": divide,
    }

    func = ops[args.operation]
    try:
        result = func(args.x, args.y)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    print(result)


if __name__ == "__main__":
    main()