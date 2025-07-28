import pandas as pd
from analyses.descriptive_stats import run as run_stats
from analyses.linear_regression import run as run_lr
from analyses.clustering import run as run_clust
import sys

def print_menu():
    print("""
Choose an analysis:
  1) Descriptive statistics
  2) Linear regression
  3) K-Means clustering
  0) Exit
""")
    return input("Enter choice: ").strip()

def main():
    path = input("Path to CSV file: ").strip()
    try:
        df = pd.read_csv(path)
    except Exception as e:
        print(f"Failed to load CSV: {e}")
        sys.exit(1)

    while True:
        choice = print_menu()
        if choice == "1":
            run_stats(df)
        elif choice == "2":
            run_lr(df)
        elif choice == "3":
            run_clust(df)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice; please try again.")

if __name__ == "__main__":
    main()
