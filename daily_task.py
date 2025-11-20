import datetime
import os
import random
import subprocess

def run_git_command(command):
    subprocess.run(command, shell=True, check=True)

def main():
    # --- 1. LAZY MODE (70% Chance to Skip) ---
    # We run 4 times a day via GitHub Actions.
    # Skipping 70% of the time means some days we might skip ALL runs (Gray/Empty day).
    if random.random() < 0.7:
        print("Decided to skip this run (Lazy Mode).")
        return

    # --- 2. DARK GREEN MODE (1 to 12 Commits) ---
    # Doing up to 12 commits ensures that even if we only run once today,
    # we can still hit the "Dark Green" threshold on the graph.
    num_commits = random.randint(1, 12)
    
    print(f"Simulating work... Preparing {num_commits} commits.")

    # --- 3. CAMOUFLAGE MESSAGES ---
    tasks = [
        "Fixed bug in authentication module",
        "Refactored CSS for mobile responsiveness",
        "Updated README documentation",
        "Optimized database queries",
        "Added unit tests for login",
        "Corrected typos in variable names",
        "Merged development branch",
        "Investigated API timeout issues",
        "Cleaned up unused imports",
        "Refactored API endpoints",
        "Updated dependency versions",
        "Improved error handling logic"
    ]

    for i in range(num_commits):
        now = datetime.datetime.now(datetime.timezone.utc)
        task = random.choice(tasks)
        
        # Writes to 'journal.md' to look like a personal coding diary
        with open("journal.md", "a") as f:
            f.write(f"## {now.strftime('%Y-%m-%d %H:%M')}\n")
            f.write(f"- {task}\n\n")
        
        # Git commands to stage and commit
        run_git_command("git add journal.md")
        run_git_command(f'git commit -m "{task}"')

    # Push all commits at once
    try:
        run_git_command("git push")
        print(f"Successfully pushed {num_commits} commits.")
    except Exception as e:
        print(f"Error pushing: {e}")

if __name__ == "__main__":
    main()