

# 🚀 99 Days of DevOps Challenge
 
**Day 03 – Linux Shell Scripting & Automation**


## What is Git and GitHub?

### 🔹 Git

* **Git** is a **distributed version control system (VCS)**.
* It tracks changes in source code, allowing multiple developers to collaborate.
* It keeps a history of changes (commits) so you can roll back, branch, and merge code safely.

### 🔹 GitHub

* **GitHub** is a **cloud platform** built on top of Git.
* It provides hosting for repositories, plus collaboration features like pull requests, issues, discussions, and workflows (CI/CD).
* It acts as a central place to share and contribute to open-source or private projects.

---

## Why Use Git & GitHub?

* To **track code changes** safely.
* To **collaborate** with other developers without overwriting each other’s work.
* To **experiment** with features (branches) without breaking the main code.
* To **store backups** of your projects in the cloud.
* To **contribute to open source** through forking and pull requests.

---

## When to Use Git & GitHub?

* **Individual projects** → for safe code history.
* **Team projects** → when multiple developers need to collaborate.
* **Open-source contributions** → to fork, clone, and submit pull requests.
* **Production-ready apps** → for CI/CD pipelines with GitHub Actions.

---

## Problems Git Solves Compared to Older Tools

| Old Tools / Approach                     | Problems                                                  | Git Solution                                                      |
| ---------------------------------------- | --------------------------------------------------------- | ----------------------------------------------------------------- |
| Centralized VCS (SVN, CVS)               | Single point of failure (server). Limited offline access. | Git is distributed → every clone has full history, works offline. |
| Manual file copy (“final\_v2\_code.zip”) | Confusing, error-prone, no history.                       | Git tracks changes with commits & branches.                       |
| Team email sharing code                  | Conflicts & overwriting files.                            | Git merges branches & resolves conflicts systematically.          |
| Lack of collaboration features           | Hard to review code or manage issues.                     | GitHub provides pull requests, issues, and workflows.             |

---

## Advantages of Git & GitHub

* Free, open-source, and widely used.
* Full offline access to history.
* Branching & merging are lightweight.
* Great collaboration and community on GitHub.
* Works with CI/CD pipelines.

## Disadvantages

* Learning curve for beginners.
* Merge conflicts can be tricky.
* Large binary files are not handled efficiently (requires Git LFS).
* GitHub private repos were paid earlier (now limited free).

---

## Bonus Read 💡 : What’s inside the .git folder?
```bash
📂 .git/
├── 📁 branches/ # Legacy, usually empty in modern Git
├── 📁 hooks/ # Client-side hooks for automating tasks (pre-commit, post-merge etc.)
├── 📁 info/ # Contains exclude file for local ignores
│ └── 📄 exclude # Like .gitignore but not committed
├── 📁 logs/ # Records history of ref updates
│ ├── 📁 refs/
│ │ ├── 📁 heads/
│ │ │ └── 📄 main # Log of changes to main branch
│ │ └── 📁 remotes/
│ │ └── 📁 origin/
│ │ └── 📄 main # Log of changes to remote tracking branch
│ └── 📄 HEAD # Log of changes to HEAD
├── 📁 objects/ # Stores all Git objects (commits, trees, blobs)
│ ├── 📁 info/
│ └── 📁 pack/ # Stores packed objects for efficiency
├── 📁 refs/ # Pointers to commit objects
│ ├── 📁 heads/
│ │ └── 📄 main # Pointer to latest commit on main
│ ├── 📁 remotes/
│ │ └── 📁 origin/
│ │ └── 📄 main # Tracks remote origin/main
│ └── 📁 tags/ # Tag references
├── 📄 config # Project-specific Git configuration
├── 📄 description # Description of the repo (used by GitWeb)
├── 📄 HEAD # Points to the current branch ref
├── 📄 index # Staging area (cached file snapshot)
├── 📄 COMMIT_EDITMSG # Stores commit message during commit
├── 📄 FETCH_HEAD # Records the branch fetched from a remote
├── 📄 ORIG_HEAD # Points to previous HEAD (useful after rebase, merge, etc.)
└── 📄 MERGE_HEAD # Present during a merge; points to the commit being merged

This .git folder is what makes a directory a Git repository. If deleted, you lose version control. 🚀

```

## Explanation of Each File and Folder:
```bash

1.branches/ (📂)
This was historically used to store branch references but is now obsolete.

2.hooks/ (📂)
Contains shell scripts that automate actions (e.g., pre-commit, post-commit, pre-push).
Default ones are .sample files to guide users.

3.info/ (📂)
Contains an exclude file for repository-specific ignored files (like .gitignore but local).

4.logs/ (📂)
Tracks movements of HEAD and branches.
Helps in recovering lost commits (git reflog).

5.objects/ (📂)
Stores actual data as blobs (file contents), trees (directories), commits, and tags.
Uses SHA-1 hashed directories for efficient storage.
pack/ stores compressed data to optimize space.

6.refs/ (📂)
Stores branch (heads/), remote (remotes/), and tag (tags/) references.
These files contain commit hashes pointing to the latest commit.

COMMIT_EDITMSG (📄)
Stores the last commit message (useful when reusing the commit message).

config (📄)
Stores repository-level configurations like remotes, user info, etc.

description (📄)
Used by GitWeb (a web-based Git viewer), but not required for regular use.

HEAD (📄)
Points to the latest commit of the currently checked-out branch.
Example: ref: refs/heads/main (means currently on main branch).

index (📄)
Stores the staging area (aka "index"), tracking what’s staged for commit.

packed-refs (📄)
If Git optimizes refs, this file consolidates them instead of storing them in separate files.

```

# 🚀 Challenges

---

## 🔹 Challenge 1: Fork and Clone an Open-Source Project

### ✅ Steps to Fork

1. Go to the GitHub repo (e.g., `https://github.com/sd031/eks-auto-mode-workshop`).
2. Click **Fork** (top-right).
3. Choose your GitHub account as the destination.
4. GitHub creates a copy under your account.

### ✅ Clone Command

```bash
git clone <https-repo-link>
```

Example:

```bash
git clone https://github.com/khanyasir1/eks-auto-mode-workshop.git
```

### ✅ Bonus – Sync with Upstream (learnt something new and intresting)

```bash
cd eks-auto-mode-workshop
git remote add upstream https://github.com/sd031/eks-auto-mode-workshop.git
```

👉 Learned: **Forking + Upstream sync is essential when contributing to open-source.**

---

## 🔹 Challenge 2: Create a Branch & Commit Changes

```bash
git checkout -b feature-branch   # create & switch
touch index.txt
echo "Hello, I am Yasir" > index.txt
git add .
git commit -m "new index file is added in feature branch"
git push origin feature-branch
```

---

## 🔹 Challenge 3: Merge Feature Branch into Main

```bash
git checkout main
git merge feature-branch
git push -u origin main
```

---

## 🔹 Challenge 4: Undo a Commit (Reset vs Revert)

###  Reset

```bash
git reset --soft <commit-id>   # keep changes staged
git reset --mixed <commit-id>  # keep changes unstaged
git reset --hard <commit-id>   # delete changes permanently
```

###  Revert

```bash
git revert <commit-id>
```

* Creates a **new commit** that undoes changes.
* Safer than reset (since history is preserved).

---

## 🔹 Challenge 5: Rebase vs Merge vs Cherry-Pick

### ✅ Rebase Command

```bash
git checkout main
git rebase feature-branch
```

### 📊 Comparison Table

| Command             | Purpose                                 | History                    | Use Case                    |
| ------------------- | --------------------------------------- | -------------------------- | --------------------------- |
| **git merge**       | Combine branches                        | Creates a merge commit     | Keep full history           |
| **git rebase**      | Replay commits on top of another branch | Linear history             | Clean project history       |
| **git cherry-pick** | Pick specific commits                   | Only chosen commits copied | Hotfix or selective feature |

---

## 🔹 Challenge 6: Create a PR on GitHub

1. Push your branch → GitHub.
2. Go to the repo → **Pull requests** tab.
3. Click **New Pull Request**.
4. Select `feature-branch → main`.
5. Add description → Create PR.

---

## 🔹 Challenge 7: Resolve Merge Conflicts

Example conflict markers:

```text
<<<<<<< HEAD
Hello from main
=======
Hello from feature-branch
>>>>>>> feature-branch
```

### ✅ Fix & Commit

```bash
nano index.txt       # manually fix conflict
git add index.txt
git commit -m "resolved merge conflict"
git push
```

---

## 🔹 Challenge 8: Git Stash

```bash
git stash push "WIP: working on feature"
git stash list
git stash apply stash@{0}
git stash pop
git stash drop stash@{0}
git stash clear
```

👉 Use Case: Temporarily save work when switching tasks.

---

## 🔹 Challenge 9: Add Version Tags

```bash
git tag v1.0.0
git push origin v1.0.0
```

👉 Tags are useful for marking releases.

---

## 🔹 Challenge 10: Edit Past Commits

### ✅ Amend Last Commit

```bash
git commit --amend -m "Updated commit message"
```

### ✅ Interactive Rebase

```bash
git rebase -i HEAD~3
```

* Opens editor:

```text
pick a1b2c3 commit message 1
pick d4e5f6 commit message 2
pick g7h8i9 commit message 3
```

Change `pick` → `edit` or `squash`.
Then modify commits.

---


## ⏭️ Next Step
👉 Tomorrow’s focus: **Day 04 – Git Advanced - Rebase, Cherry-pick, Conflict Resolution**
---
📌 Resource: [ **Day 04 – Git Advanced - Rebase, Cherry-pick, Conflict Resolution**](https://www.learnxops.com/git-advanced-rebase-cherry-pick-conflict-resolution/)
