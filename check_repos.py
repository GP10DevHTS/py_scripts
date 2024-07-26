import os
import subprocess

def check_repo_status(repo_path):
    try:
        # Change directory to the repository path
        os.chdir(repo_path)
        
        # Fetch the latest changes from the remote repository
        subprocess.run(['git', 'fetch'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Check the status of the local repository against the remote
        status = subprocess.run(['git', 'status', '-uno'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if "Your branch is up to date" in status.stdout:
            return "Up to date"
        elif "Your branch is behind" in status.stdout:
            return "Not up to date"
        else:
            return "Unable to determine status or no tracking information"
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    base_dir = 'C:/xampp/htdocs'
    directories = os.listdir(base_dir)
    
    for directory in directories:
        repo_path = os.path.join(base_dir, directory)
        if os.path.isdir(repo_path):
            # Check if the directory is a git repository
            if os.path.exists(os.path.join(repo_path, '.git')):
                status = check_repo_status(repo_path)
                print(f"{directory}: {status}")
            else:
                print(f"{directory}: Not a git repository")

if __name__ == "__main__":
    main()
