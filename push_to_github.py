import subprocess
import sys

def git_push(repo_path, commit_message="Update algo_output.xlsx"):
    try:
        # Change directory to your repo folder
        subprocess.check_call(['git', '-C', repo_path, 'add', 'algo_output.xlsx'])
        subprocess.check_call(['git', '-C', repo_path, 'commit', '-m', commit_message])
        subprocess.check_call(['git', '-C', repo_path, 'push'])
        print("Pushed changes successfully!")
    except subprocess.CalledProcessError as e:
        print("Error during Git operations:", e)
        sys.exit(1)

if __name__ == "__main__":
    repo_folder = r"C:\API CONNECTION\Fyers\Stock-screener"
    git_push(repo_folder)
