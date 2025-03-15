# Palindrome Number

## Problem Description

Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.

An integer is a palindrome when it reads the same backward as forward.

For example, `121` is a palindrome while `123` is not.

## Examples

```
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
```

```
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it reads 121-. Therefore it is not a palindrome.
```

```
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```

## Solution Requirements

Create a function named `solution` that:
- Takes an integer as input
- Returns a boolean (true if the integer is a palindrome, false otherwise)

## Running Tests

```bash
python tests/runner.py solutions/{solution-file}
```