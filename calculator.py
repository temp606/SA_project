"""Simple calculator application.

Provides basic arithmetic operations (add, subtract, multiply, divide, floor divide) and
advanced operations (power, modulus). Can be used as a module or from the command line.
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

def power(a: float, b: float) -> float:
    """Raise a to the power of b.
    
    Args:
        a: Base value
        b: Exponent
        
    Returns:
        a raised to the power of b
        
    Raises:
        ValueError: If base is 0 and exponent is 0 (undefined in mathematics)
        ValueError: If base is 0 and exponent is negative (undefined)
    """
    if a == 0 and b == 0:
        raise ValueError("Cannot compute 0**0 (undefined)")
    if a == 0 and b < 0:
        raise ValueError("Cannot compute 0 to a negative power (undefined)")
    return a ** b

def modulus(a: float, b: float) -> float:
    """Compute a modulo b.
    
    Args:
        a: Dividend
        b: Divisor
        
    Returns:
        Remainder of a divided by b
        
    Raises:
        ValueError: If divisor is 0
        
    Note:
        In Python, modulus with negative values follows the convention:
        The result has the same sign as the divisor b.
        Example: -7 % 3 = 2, 7 % -3 = -2
    """
    if b == 0:
        raise ValueError("Cannot modulus by zero")
    return a % b

def floor_divide(a: float, b: float) -> float:
    """Compute the floor division of a by b.
    
    Args:
        a: Dividend
        b: Divisor
        
    Returns:
        The largest integer less than or equal to a divided by b
        
    Raises:
        ValueError: If divisor is 0
    """
    if b == 0:
        raise ValueError("Cannot floor divide by zero")
    return a // b


def main():
    parser = argparse.ArgumentParser(
        description="Simple calculator CLI: performs arithmetic (add, sub, mul, div, floordiv) and advanced (pow, mod) operations"
    )
    parser.add_argument("x", type=float, help="First operand")
    parser.add_argument("y", type=float, help="Second operand")
    parser.add_argument(
        "operation",
        choices=["add", "sub", "mul", "div", "floordiv", "pow", "mod"],
        help="Operation to perform: add, sub, mul, div, floordiv (floor division), pow (power/exponentiation), mod (modulus)",
    )
    args = parser.parse_args()

    ops = {
        "add": add,
        "sub": subtract,
        "mul": multiply,
        "div": divide,
        "floordiv": floor_divide,
        "pow": power,
        "mod": modulus,
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