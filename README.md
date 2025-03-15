# Leetcode Solutions

Project structure for solving and testing coding challenges in multiple languages.

## Structure

```
problems/
├── problem-name/
│   ├── README.md        # Problem description and instructions
│   ├── solutions/       # Solution implementations
│   │   ├── solution.py  # Python solution
│   │   ├── solution.js  # JavaScript solution
│   │   └── ...          # Other language solutions
│   └── tests/           # Language-agnostic tests
│       ├── test_cases.json  # Test cases in JSON format
│       └── runner.py        # Test runner that executes any solution
```

## Adding a New Problem

1. Create a directory in `problems/` with the problem name
2. Add a README.md with the problem description
3. Create solutions in different languages in the `solutions/` directory
4. Add test cases in `tests/test_cases.json`

## Running Tests

```bash
python problems/{problem-name}/tests/runner.py {solution-file}
```