"""Main entry point for the Problem of the Day solver."""
from typing import Optional
from .problem_fetcher import fetch_problem, ProblemDetails
from .solution_generator import generate_solution, Solution
from .config import SECTION_SEPARATOR

def main():
    """Main function to run the problem solver."""
    # Get platform choice
    platform = input("Choose platform (leetcode/geeksforgeeks): ").strip().lower()
    
    # Fetch problem
    problem = fetch_problem(platform)
    if not problem:
        print("Could not fetch problem. Please try again later.")
        return
    
    # Display problem details
    _display_problem(problem)
    
    # Generate solution
    solution = generate_solution(problem)
    if not solution:
        print("Could not generate solution. Please try again later.")
        return
    
    # Display solution
    _display_solution(solution)

def _display_problem(problem: ProblemDetails):
    """Display problem details in a formatted manner."""
    print(SECTION_SEPARATOR)
    print(f"Problem: {problem.title}")
    print(f"Difficulty: {problem.difficulty}")
    print("\nDescription:")
    print(problem.description)
    print("\nConstraints:")
    for constraint in problem.constraints:
        print(f"- {constraint}")
    print("\nExamples:")
    for i, example in enumerate(problem.examples, 1):
        print(f"\nExample {i}:")
        print(f"Input: {example['input']}")
        print(f"Output: {example['output']}")

def _display_solution(solution: Solution):
    """Display solution details in a formatted manner."""
    print(SECTION_SEPARATOR)
    print("Solution:")
    print("\nImplementation:")
    print(solution.code)
    print("\nExplanation:")
    print(solution.explanation)
    print("\nComplexity Analysis:")
    print(f"Time Complexity: {solution.time_complexity}")
    print(f"Space Complexity: {solution.space_complexity}")
    print("\nTest Cases:")
    for i, test in enumerate(solution.test_cases, 1):
        print(f"\nTest {i}:")
        print(f"Input: {test['input']}")
        print(f"Expected: {test['expected']}")
        print(f"Output: {test['output']}")

if __name__ == "__main__":
    main()