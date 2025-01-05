"""Main entry point for the Problem of the Day launcher."""
from src.launcher import launch_platform

def main():
    """Main function to run the launcher."""
    while True:
        print("\nProblem of the Day Launcher")
        print("1. LeetCode")
        print("2. GeeksforGeeks")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            launch_platform("leetcode")
        elif choice == "2":
            launch_platform("geeksforgeeks")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()