#!/usr/bin/env python3
import os
import sys
import shutil
from pathlib import Path

def create_problem(problem_name):
    # Convert problem name to kebab-case
    problem_slug = problem_name.lower().replace(" ", "-")
    
    # Define paths
    base_dir = Path(__file__).parent
    template_dir = base_dir / "template"
    problem_dir = base_dir / "problems" / problem_slug
    
    # Check if problem already exists
    if problem_dir.exists():
        print(f"Error: Problem '{problem_slug}' already exists.")
        return False
    
    # Create problem directory structure
    problem_dir.mkdir(parents=True, exist_ok=True)
    (problem_dir / "solutions").mkdir(exist_ok=True)
    (problem_dir / "tests").mkdir(exist_ok=True)
    
    # Copy template files
    shutil.copy(template_dir / "README.md", problem_dir / "README.md")
    shutil.copy(template_dir / "tests" / "test_cases.json", problem_dir / "tests" / "test_cases.json")
    shutil.copy(template_dir / "tests" / "runner.py", problem_dir / "tests" / "runner.py")
    shutil.copy(template_dir / "solutions" / "solution.py", problem_dir / "solutions" / "solution.py")
    shutil.copy(template_dir / "solutions" / "solution.js", problem_dir / "solutions" / "solution.js")
    
    # Update README title with problem name
    readme_path = problem_dir / "README.md"
    with open(readme_path, 'r') as f:
        content = f.read()
    
    content = content.replace("[Problem Name]", problem_name)
    
    with open(readme_path, 'w') as f:
        f.write(content)
    
    print(f"Problem '{problem_name}' created successfully at {problem_dir}")
    print("Next steps:")
    print("1. Update the problem description in README.md")
    print("2. Add test cases in tests/test_cases.json")
    print("3. Implement your solution in solutions/solution.py or solutions/solution.js")
    
    return True

def main():
    if len(sys.argv) < 2:
        print("Usage: python create_problem.py <problem-name>")
        return 1
    
    problem_name = " ".join(sys.argv[1:])
    create_problem(problem_name)
    return 0

if __name__ == "__main__":
    sys.exit(main())