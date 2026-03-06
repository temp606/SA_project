# Simple Calculator Application

A robust Python calculator with support for basic arithmetic and advanced operations, including comprehensive edge case handling.

## Features

- **Basic Operations**: Addition, subtraction, multiplication, division, floor division
- **Advanced Operations**: Power (exponentiation), modulus
- **Error Handling**: Validates division by zero, modulus by zero, and undefined mathematical operations
- **CLI Interface**: Easy-to-use command-line interface
- **Type Safety**: Full type hints throughout the codebase
- **Comprehensive Tests**: 14 unit tests covering normal and edge cases

## Installation

### Requirements
- Python 3.7+
- pytest (for running tests)

### Setup
```bash
# Clone or navigate to the project directory
cd /Users/manideepboddu/Temp

# Install test dependencies (optional)
pip install pytest
```

## Usage

### Command Line Interface

```bash
python calculator.py <operand1> <operand2> <operation>
```

#### Supported Operations
- `add` - Addition
- `sub` - Subtraction
- `mul` - Multiplication
- `div` - Division
- `floordiv` - Floor division
- `pow` - Power/Exponentiation
- `mod` - Modulus

#### Examples
```bash
# Addition
python calculator.py 5 3 add
# Output: 8.0

# Subtraction
python calculator.py 10 4 sub
# Output: 6.0

# Multiplication
python calculator.py 6 7 mul
# Output: 42.0

# Division
python calculator.py 10 2 div
# Output: 5.0

# Floor Division
python calculator.py 10 3 floordiv
# Output: 3.0

# Power
python calculator.py 2 3 pow
# Output: 8.0

# Modulus
python calculator.py 10 3 mod
# Output: 1.0
```

### Using as a Module

```python
from calculator import add, subtract, multiply, divide, floor_divide, power, modulus

# Basic operations
result = add(5, 3)              # 8
result = subtract(10, 4)        # 6
result = multiply(6, 7)         # 42
result = divide(10, 2)          # 5.0
result = floor_divide(10, 3)    # 3.0

# Advanced operations
result = power(2, 3)            # 8
result = modulus(10, 3)         # 1
```

## Edge Cases & Validation

### Power Function
- **0**0**: Raises `ValueError` (mathematically undefined)
- **0 to negative power**: Raises `ValueError` (undefined)
- **Valid cases**: `2**3 = 8`, `5**0 = 1`, `2**-1 = 0.5`

Example:
```python
power(0, 0)   # Raises ValueError: Cannot compute 0**0 (undefined)
power(0, -1)  # Raises ValueError: Cannot compute 0 to a negative power (undefined)
power(2, 3)   # Returns 8.0
```

### Modulus Function
- **Division by zero**: Raises `ValueError`
- **Negative values**: Follows Python convention where result sign matches the divisor
  - `-7 % 3 = 2` (positive divisor → positive result)
  - `7 % -3 = -2` (negative divisor → negative result)
  - `-7 % -3 = -1` (both negative → result follows divisor)

Example:
```python
modulus(10, 3)   # Returns 1
modulus(-7, 3)   # Returns 2
modulus(7, -3)   # Returns -2
modulus(-7, -3)  # Returns -1
```

### Division Function
- **Division by zero**: Raises `ValueError`

### Floor Division Function
- **Division by zero**: Raises `ValueError`
- **Returns integer result**: `10 // 3 = 3.0`, `-7 // 2 = -4.0`

Example:
```python
floor_divide(10, 3)   # Returns 3.0
floor_divide(-7, 2)   # Returns -4.0 (rounds down toward negative infinity)
floor_divide(7, 2)    # Returns 3.0
```

## Testing

Run the test suite:

```bash
# Run all tests
pytest test_calculator.py -v

# Run with coverage
pytest test_calculator.py --cov=calculator

# Run specific test
pytest test_calculator.py::test_power_zero_to_zero -v
```

### Test Coverage
The test suite includes 14 tests covering:
- ✅ Basic arithmetic operations
- ✅ Division by zero validation
- ✅ Power function with normal, zero, and negative exponents
- ✅ 0**0 edge case
- ✅ 0 to negative power edge case
- ✅ Modulus with positive, negative, and mixed operands
- ✅ Modulus by zero validation

All tests pass successfully.

## Project Structure

```
.
├── calculator.py          # Main calculator module with all operations
├── test_calculator.py     # Unit tests for all functions
└── README.md             # This file
```

## Error Handling

The calculator provides clear error messages for invalid operations:

```bash
# Division by zero
python calculator.py 5 0 div
# Error: Cannot divide by zero

# Modulus by zero
python calculator.py 5 0 mod
# Error: Cannot modulus by zero

# 0 to the power of 0
python calculator.py 0 0 pow
# Error: Cannot compute 0**0 (undefined)
```

## Design Decisions

1. **Float arithmetic**: All operations use floats for consistency and to support decimal inputs
2. **Python modulus semantics**: The modulus function follows Python's convention where the result sign matches the divisor
3. **Explicit error handling**: Edge cases like 0**0 raise clear exceptions rather than attempting silent fallbacks
4. **Type hints**: All functions include type hints for better IDE support and code clarity

## Contributing

To extend the calculator with additional operations:

1. Add the operation function to `calculator.py`
2. Add comprehensive tests to `test_calculator.py`
3. Update the CLI argument parser with the new operation
4. Update this README with examples

## License

This is a simple educational calculator application.
