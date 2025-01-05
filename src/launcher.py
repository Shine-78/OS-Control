"""Main launcher for Problem of the Day navigation."""
import webbrowser
from .browser_automation import navigate_gfg_problem
from .config import LEETCODE_URL
import sys

def launch_platform(platform: str) -> None:
    """Launch the specified coding platform."""
    platform = platform.lower()
    
    try:
        if platform == "leetcode":
            print("Opening LeetCode Problem of the Day...")
            webbrowser.open(LEETCODE_URL, new=2)
        elif platform == "geeksforgeeks":
            print("Opening GeeksForGeeks Problem of the Day with automation...")
            navigate_gfg_problem()
        else:
            print(f"Error: Unsupported platform. Choose from: leetcode, geeksforgeeks")
    except Exception as e:
        print(f"Error launching platform: {str(e)}")
        sys.exit(1)