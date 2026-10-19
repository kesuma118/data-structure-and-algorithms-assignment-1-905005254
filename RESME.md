# Stack-Based Expression Evaluator

**Course:** DCOMP320 Data Structures and Algorithm
**Assignment:** Stacks Implementation

This Python program reads mathematical expressions from `input.txt`, evaluates each one using a stack, and writes the results to `output.txt`.

## Requirements
- Python 3.8 or newer. No extra libraries are needed.

## How to run
1. Put `stack_evaluator.py` and `input.txt` in the same folder.
2. Open a terminal in that folder and run:
   ```
   python stack_evaluator.py
   ```
3. Open `output.txt` to see the results.

To use other file names:
```
python stack_evaluator.py my_input.txt my_output.txt
```

To run the tests:
```
python test_stack_evaluator.py
```

## Input file format
- One expression per line.
- Expressions are separated by a line containing only dashes (three or more), for example `-----`.
- Supported: whole numbers, decimals, `+ - * /`, parentheses `( )`, and a leading minus such as `-5`.

Example `input.txt`:
```
3 + 5 * 2
-----
(8 / 4) + 7 * 2
-----
10 - (2 + 3) * 4
```

## Output file format
- One result per line, separated by the same separator line used in the input.
- Whole-number results have no decimal point (`13`, not `13.0`).
- An invalid expression produces a line such as `Error: division by zero` and the program continues with the next expression.

Example `output.txt`:
```
13
-----
16
-----
-10
```

## How it works
- `Stack` class with `push`, `pop`, `peek`, `is_empty` and `size`.
- `evaluate()` uses two stacks, one for numbers and one for operators. Operators with higher precedence are applied first, and brackets are resolved when `)` is reached.
- `process_file()` reads the input file, evaluates every expression and writes the output file.

## Assumptions and limitations
- Supported operators are only `+`, `-`, `*`, `/` (no powers, functions or variables).
- Division uses normal (decimal) division, so `7 / 2` gives `3.5`.
- Decimal results are rounded to 6 decimal places.
- Blank lines in the input file are ignored.
- Invalid expressions (unbalanced brackets, division by zero, missing operands, unknown characters) are reported as `Error: ...` in the output.
