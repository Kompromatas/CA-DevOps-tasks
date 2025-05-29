# CA-DevOps-tasks
CA DevOps course tasks assigned repo
## Git Commands with Detailed Examples

### 1. Clone a Repository
```sh
git clone https://github.com/username/repository.git
```
Clones the remote repository to your local machine.

### 2. Check Repository Status
```sh
git status
```
Shows the status of changes as untracked, modified, or staged.

### 3. Add Files to Staging Area
```sh
git add filename.txt
```
Stages a specific file for commit.

To add all files:
```sh
git add .
```

### 4. Commit Changes
```sh
git commit -m "Describe your changes"
```
Commits staged changes with a message.

### 5. Push Changes to Remote
```sh
git push origin main
```
Pushes your commits to the `main` branch on the remote repository.

### 6. Pull Latest Changes
```sh
git pull origin main
```
Fetches and merges changes from the remote `main` branch.

### 7. Create and Switch to a New Branch
```sh
git checkout -b feature-branch
```
Creates and switches to a new branch named `feature-branch`.

### 8. Merge a Branch
```sh
git checkout main
git merge feature-branch
```
Merges `feature-branch` into `main`.

### 9. View Commit History
```sh
git log
```
Displays the commit history for the repository.

### 10. Discard Local Changes
```sh
git checkout -- filename.txt
```
Reverts changes in a file to the last committed state.