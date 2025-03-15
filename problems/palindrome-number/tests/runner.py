#!/usr/bin/env python3
import json
import sys
import os
import subprocess
import importlib.util
from pathlib import Path

def load_test_cases(test_file):
    with open(test_file, 'r') as f:
        return json.load(f)

def run_python_solution(solution_path, test_cases):
    # Import the module dynamically
    spec = importlib.util.spec_from_file_location("solution", solution_path)
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    
    # Assuming the function is called "solution"
    results = []
    for tc in test_cases:
        result = solution.solution(tc["input"])
        results.append({
            "input": tc["input"],
            "expected": tc["expected"],
            "actual": result,
            "passed": result == tc["expected"]
        })
    return results

def run_javascript_solution(solution_path, test_cases):
    # Create a temporary JS file to run the solution
    temp_js = """
const solution = require('${solution_path}');
const testCases = ${test_cases};

const results = testCases.map(tc => {
    const result = solution(tc.input);
    return {
        input: tc.input,
        expected: tc.expected,
        actual: result,
        passed: result === tc.expected
    };
});

console.log(JSON.stringify(results));
""".replace("${solution_path}", solution_path).replace("${test_cases}", json.dumps(test_cases))
    
    with open("temp_runner.js", "w") as f:
        f.write(temp_js)
    
    # Run the JS file
    result = subprocess.run(["node", "temp_runner.js"], capture_output=True, text=True)
    os.remove("temp_runner.js")
    
    return json.loads(result.stdout)

def main():
    if len(sys.argv) < 2:
        print("Usage: python runner.py <solution_file>")
        sys.exit(1)
    
    solution_path = sys.argv[1]
    
    # Get directory of this script
    script_dir = Path(__file__).parent
    test_file = script_dir / "test_cases.json"
    
    # Load test cases
    test_cases = load_test_cases(test_file)
    
    # Determine language and run solution
    if solution_path.endswith(".py"):
        results = run_python_solution(solution_path, test_cases)
    elif solution_path.endswith(".js"):
        results = run_javascript_solution(solution_path, test_cases)
    else:
        print(f"Unsupported file extension for {solution_path}")
        sys.exit(1)
    
    # Display results
    passed = 0
    for i, r in enumerate(results):
        status = "✅" if r["passed"] else "❌"
        print(f"Test {i+1}: {status} Input: {r['input']}, Expected: {r['expected']}, Got: {r['actual']}")
        if r["passed"]:
            passed += 1
    
    print(f"\nSummary: {passed}/{len(results)} tests passed")
    
    if passed < len(results):
        sys.exit(1)

if __name__ == "__main__":
    main()