# 🚀 99 Days of DevOps Challenge

**Day 04 – Git Advanced: Rebase, Cherry-pick, Conflict Resolution**

---

## 🔹 Git Rebase

### 📌 What is Rebase?

* Rebase is the process of moving or combining a sequence of commits onto a new base commit.
* It rewrites commit history to create a **linear, clean history**.

### 📌 When to Use?

* When you want a **clean commit history** (no merge commits).
* When your feature branch has diverged from `main` and you want to sync with it.

### 📌 Why Use?

* To make history look like a straight line → easy to read & debug.
* Removes unnecessary merge commits.

### 📌 How to Use?

```bash
git checkout feature-branch
git rebase main
```

👉 This takes all commits from `feature-branch` and re-applies them on top of `main`.

### 📊 Merge vs Rebase

| Command    | History Style                     | Use Case                  |
| ---------- | --------------------------------- | ------------------------- |
| **Merge**  | Keeps all branches + merge commit | Preserve full history     |
| **Rebase** | Linear history                    | Clean, simplified history |

---

## 🔹 Git Cherry-pick

### 📌 What is Cherry-pick?

* Cherry-pick allows you to **copy a single commit** (or a few) from one branch and apply it to another branch.

### 📌 When to Use?

* When you need a **specific fix/feature** from another branch without merging the whole branch.

### 📌 Why Use?

* Helps in **hotfixes** – e.g., apply one bug fix from `dev` to `production`.

### 📌 How to Use?

```bash
git checkout main
git cherry-pick <commit-hash>
```

👉 Only that commit will be copied into `main`.

### 📊 Rebase vs Cherry-pick

| Feature  | Rebase                                 | Cherry-pick                    |
| -------- | -------------------------------------- | ------------------------------ |
| Purpose  | Replay **all commits** onto new branch | Copy **specific commits** only |
| History  | Linear + modified                      | Keeps separate commits         |
| Use Case | Sync feature branch with main          | Apply a hotfix to production   |

---

## 🔹 Git Conflict Resolution

### 📌 What is a Conflict?

* A **conflict** happens when Git cannot automatically merge/rebase because the same part of a file was changed in two branches.

### 📌 When to Use?

* During **merge** or **rebase**, when Git asks you to resolve conflicts manually.

### 📌 Why Use?

* To make sure the final code reflects the correct changes, not overwritten ones.

### 📌 How to Resolve?

1. Open the conflicted file:

```text
<<<<<<< HEAD
Code from current branch
=======
Code from other branch
>>>>>>> feature-branch
```

2. Edit file manually to keep/fix correct version.
3. Mark conflict as resolved:

```bash
git add <file>
git commit
```

---

## 🔹 Git Reset vs Git Revert

### 📌 Git Reset

* Moves `HEAD` (and sometimes staging/working directory) to an earlier commit.
* Types:

  * `--soft` → Keeps changes staged.
  * `--mixed` → Keeps changes unstaged.
  * `--hard` → Discards all changes (dangerous).

```bash
git reset --soft <commit>
git reset --hard <commit>
```

### 📌 Git Revert

* Creates a **new commit** that undoes the changes of a specific commit.
* Safer because history is preserved.

```bash
git revert <commit>
```

### 📊 Reset vs Revert

| Command        | Effect                                | Safety |
| -------------- | ------------------------------------- | ------ |
| **git reset**  | Moves HEAD back, can remove commits   | Risky  |
| **git revert** | Adds a new commit that undoes changes | Safe   |

---

## 🔹 Git Commit Amend

* Used to **change the last commit** (message or files).
* Helpful if you forgot to add a file or need to fix the commit message.

```bash
git add forgotten-file
git commit --amend -m "Updated commit message"
```

⚠️ Only use before pushing to remote (to avoid conflicts).

---

## 🔹 Git Hooks

* Git hooks are scripts that run automatically on events like commit, push, or merge.
* Common hook: **pre-commit** → run linting/tests before committing.

```bash
# Example pre-commit hook
#!/bin/sh
echo "Running pre-commit checks..."
npm run lint
```

Stored in: `.git/hooks/`

---


# 🔹 Challenge 1: Perform an Interactive Rebase to Modify Commit History

### 📝 What is Interactive Rebase?

Interactive Rebase (`git rebase -i`) allows you to **edit commit history**. You can:

* Change commit messages (reword).
* Edit commit content (edit).
* Combine multiple commits into one (squash).
* Reorder commits.

---

### 🚀 When to Use It?

* **Before pushing a branch** → Clean up commit history.
* **Before opening a Pull Request** → Convert multiple small “WIP” commits into one meaningful commit.
* **Fix mistakes in past commits** → Add/remove changes or rename messages.
* **Reorder commits** → Change the logical sequence of commits.

⚠️ **Important:** Never rebase commits that are already pushed to a shared/public branch. It rewrites history and may cause issues for collaborators.

---

## ✅ Steps to Perform Interactive Rebase

### Step 1: Start Interactive Rebase

Choose how many commits you want to edit. Example: last 4 commits.

```bash
git rebase -i HEAD~4
```

This opens a **rebase todo file** in your default editor, showing something like:

```
pick a30c19e Added index page
pick bb4cc8d Fixed typo in docs
pick d0dd1f6 Final cleanup
pick e4f11a7 Updated CSS
```

Here:

* Commits are listed from **oldest (top)** to **newest (bottom)**.
* Each line starts with the action `pick`.

---

### Step 2: Choose an Action

#### 🔹 1. Reword (Rename Commit Message)

If you just want to change a commit message:

1. Replace `pick` with `reword`.

   ```
   reword a30c19e Added index page
   pick bb4cc8d Fixed typo in docs
   pick d0dd1f6 Final cleanup
   pick e4f11a7 Updated CSS
   ```
2. Save & close the file.
3. A new editor window will open for that commit → type the new commit message.
4. Save & close → Done ✅

---

#### 🔹 2. Edit (Modify Commit Content)

If you want to change files inside a commit:

1. Replace `pick` with `edit`.

   ```
   edit a30c19e Added index page
   pick bb4cc8d Fixed typo in docs
   pick d0dd1f6 Final cleanup
   pick e4f11a7 Updated CSS
   ```
2. Save & close. Git will stop at that commit.
3. Make your changes (edit file, add/remove code).
4. Stage the changes:

   ```bash
   git add <file>
   ```
5. Continue rebase:

   ```bash
   git rebase --continue
   ```

---

#### 🔹 3. Squash (Combine Commits)

If you want to merge multiple commits into one:

1. Keep the first commit as `pick`, and mark the following ones as `squash`.

   ```
   pick a30c19e Added index page
   squash bb4cc8d Fixed typo in docs
   squash d0dd1f6 Final cleanup
   pick e4f11a7 Updated CSS
   ```
2. Save & close.
3. Git will open a new editor window with **all commit messages** → keep/edit them into one final message.
4. Save & close → Commits are merged into one ✅

⚠️ **Be careful:**

* Commits are in order from **oldest → newest**.
* If you try to squash the **first commit** (oldest one), Git will throw an error:

  ```
  Cannot squash without a previous commit
  ```

---

#### 🔹 4. Reorder (Change Commit Order)

If you want to rearrange commits:

* Simply cut/paste lines inside the todo file.

**Original Order:**

```
pick a30c19e Added index page
pick bb4cc8d Fixed typo in docs
pick d0dd1f6 Final cleanup
```

**New Order (Commit C moved up):**

```
pick a30c19e Added index page
pick d0dd1f6 Final cleanup
pick bb4cc8d Fixed typo in docs
```

1. Save & close.
2. Git will reapply commits in the new order.
3. If conflicts occur → resolve them, then run:

   ```bash
   git add <files>
   git rebase --continue
   ```

---

## 🔹 Challenge 2: Use `git cherry-pick` to apply a specific commit from another branch to your current branch

**Goal:** Copy a single useful commit from `git-adv-practice` (or any source branch) and apply it to `main` (or any target branch) without merging the whole source branch.

---

### ✅ Pre-check / Preparation

1. Make sure your working tree is clean (commit or stash any changes).

```bash
git status
```

2. Ensure remotes are up to date:

```bash
git fetch origin
```

---

### ✅ Step 1 — Identify the commit to cherry-pick

List commits on the source branch to find the SHA you want:

```bash
git log git-adv-practice --oneline --graph --decorate
```

Example output (assume we want the second commit `89ba37c`):

```
6a43be4 task-01 done merge conflict
89ba37c task-01 done merge conflict  <-- pick this one
...
```

---

### ✅ Step 2 — Switch to the target branch

Switch to the branch where you want the commit to land (`main` in this example) and ensure it's up-to-date:

```bash
git checkout main
git pull origin main
```

---

### ✅ Step 3 — Perform the cherry-pick

Apply the specific commit by SHA:

```bash
git cherry-pick 89ba37c
```

**What happens:**

* Git will try to apply the patch of `89ba37c` on top of `main`.
* If it applies cleanly, Git creates a **new commit** on `main` (new SHA) but preserves the original author and message by default.

**Example success message:**

```
[main 1a2b3c4] task-01 done merge conflict
 1 file changed, X insertions(+)
```

---

### ✅ Step 4 — If a conflict occurs

If the commit overlaps with changes on `main`, you may see:

```
error: could not apply 89ba37c... task-01 done merge conflict
hint: Fix them up in the work tree, and then use 'git add/rm <file>'
```

**Resolve conflicts:**

1. Open the conflicted file(s). You will see conflict markers:

   ```text
   <<<<<<< HEAD
   (current branch content)
   =======
   (incoming commit content)
   >>>>>>> 89ba37c
   ```
2. Edit the file to produce the final desired content, then remove the conflict markers.
3. Stage the resolved file(s):

   ```bash
   git add README.md
   ```
4. Continue the cherry-pick:

   ```bash
   git cherry-pick --continue
   ```

   * If you decide you cannot resolve / want to abort:

     ```bash
     git cherry-pick --abort
     ```
   * If you want to skip this problematic commit and continue (rare for single-commit cherry-pick):

     ```bash
     git cherry-pick --skip
     ```

---

### ✅ Extra useful cherry-pick options

* Apply but don’t create commit immediately (so you can modify content before committing):

  ```bash
  git cherry-pick --no-commit 89ba37c
  # edit files if needed
  git commit -m "Adjusted cherry-picked changes: <message>"
  ```
* Record the original commit reference in the new commit message (helps traceability):

  ```bash
  git cherry-pick -x 89ba37c
  ```

  This appends `(cherry picked from commit 89ba37c...)` to the commit message.

---

### ✅ Step 5 — Push the result

After cherry-pick completes and you’re happy:

```bash
git push origin main
```

> If you rebased or force-synced remote earlier and you rewrote history, be careful with force-push. For normal cherry-pick to a tip of main, regular push is fine.

---

### ⚠️ Warnings & Tips

* Cherry-pick creates a **new commit** on the target branch — the SHA will differ from the original.
* If the commit you cherry-pick depends on earlier commits (context, helper functions, file renames), cherry-picking that single commit may fail or produce an incomplete patch — consider cherry-picking all dependent commits or merging the branch instead.
* Use `git cherry-pick -x` for traceability when backporting or applying hotfixes.
* Prefer `git cherry-pick` for isolated fixes / hotfixes. For full feature transfer or many dependent commits, consider merging or rebasing the whole feature branch.
* If you must update a shared branch after rewriting commits elsewhere, use `--force-with-lease` carefully (coordinate with your team).

---

### ✅ Example flow (quick recap)

```bash
# 1. Fetch and inspect source branch
git fetch origin
git log git-adv-practice --oneline

# 2. Checkout target branch and update
git checkout main
git pull origin main

# 3. Cherry-pick the commit
git cherry-pick 89ba37c

# 4. If conflicts:
#  - resolve files, git add <file>
#  - then:
git cherry-pick --continue
# or, to abort:
git cherry-pick --abort

# 5. Push
git push origin main
```

---


# 🚀 Challenge 3: Create a Merge Conflict and Resolve It (Merge & Rebase)

---

## Step 1: Create a Conflict Scenario

We’ll force a conflict by editing the **same line in the same file** on two different branches.

### On `main` branch:

```bash
# Switch to main branch
git checkout main

# Edit README.md (example: change Line 5)
echo "This is the MAIN branch version." > README.md
git add README.md
git commit -m "MAIN: change README.md line"
```

### On `feature-01` branch:

```bash
# Switch to feature-01
git checkout feature-01

# Edit the SAME line in README.md but with different content
echo "This is the FEATURE branch version!" > README.md
git add README.md
git commit -m "FEATURE: conflicting change in README.md"
```

✅ Now both branches (`main` and `feature-01`) have **different edits on the same line** → a guaranteed conflict.

---

## Solution A: Resolve Conflict with `git merge`

1. **Switch to `main`:**

   ```bash
   git checkout main
   ```

2. **Merge feature branch:**

   ```bash
   git merge feature-01
   ```

   Output will show:

   ```
   CONFLICT (content): Merge conflict in README.md
   Automatic merge failed; fix conflicts and then commit the result.
   ```

3. **Open `README.md`:** You’ll see conflict markers:

   ```txt
   <<<<<<< HEAD
   This is the MAIN branch version.
   =======
   This is the FEATURE branch version!
   >>>>>>> feature-01
   ```

4. **Resolve manually:** Keep one version or combine both. Example:

   ```txt
   This is the FEATURE branch version!
   ```

5. **Mark as resolved and commit:**

   ```bash
   git add README.md
   git commit
   ```

✅ Done! The merge is complete with a new **merge commit** in history.

---

## Solution B: Resolve Conflict with `git rebase`

Rebasing creates **linear history** (no merge commits).

1. **Switch to feature branch:**

   ```bash
   git checkout feature-01
   ```

2. **Rebase on top of main:**

   ```bash
   git rebase main
   ```

   Output:

   ```
   CONFLICT (content): Merge conflict in README.md
   error: could not apply [commit-id]... FEATURE: conflicting change
   ```

3. **Open `README.md`:** Same conflict markers appear, but during rebase.

4. **Resolve manually, stage and continue:**

   ```bash
   git add README.md
   git rebase --continue
   ```

✅ Done! Now the history is **clean & linear**, as if the feature branch commits were written directly after `main`.

---

### ⚡ Key Difference

* **Merge** → Adds an extra *merge commit*. History looks like a tree with branches joined.
* **Rebase** → No extra commit, history looks like a straight line (linear).



---

# 🚀 Challenge 4: Undo a Commit (`git reset` vs `git revert`)

Undoing commits in Git can be done in **two main ways**:

1. `git reset` → **Rewrites history** (dangerous for public branches).
2. `git revert` → **Safe undo**, creates a new commit that reverses a previous one.

---

## ⚡ Key Differences

| Command          | What it Does                                                                 | When to Use / Safety                 |
| ---------------- | ---------------------------------------------------------------------------- | ------------------------------------ |
| **`git reset`**  | Rewrites commit history. Commits are **permanently removed**.                | Only for **local/unpushed commits**. |
| **`git revert`** | Preserves history. Creates a **new commit** that undoes the previous commit. | Safe for **public/pushed commits**.  |

---

## Part A: `git reset` (Rewriting History)

`git reset` has **three main modes**, defining where the changes go after undoing a commit.

### Example: Last 3 commits

```
8e28244 (HEAD -> main) Commit 3: Added file C
eb3dffa Commit 2: Added file B
4f85dd4 Commit 1: Added file A
```

We will undo **Commit 3** (`8e28244`).

---

### 1. `git reset --soft [Commit ID]`

* **What it does:** Undo commit history, but **keeps changes staged**.
* **Result:** Files remain in **staging area**, ready to commit again.

```bash
git reset --soft eb3dffa
# Changes from Commit 3 are still staged.
```

---

### 2. `git reset --mixed [Commit ID]` (default)

* **What it does:** Undo commit history, moves changes to **working directory**, **clears staging area**.
* **Result:** Files are visible but **unstaged**, ready for `git add` and commit.

```bash
git reset --mixed eb3dffa
# Changes from Commit 3 are now in working directory (unstaged).
```

---

### 3. `git reset --hard [Commit ID]`

* **What it does:** Undo commit history **and deletes all changes** from staging and working directory.
* **Result:** Files and history match the target commit exactly. **All later changes are lost.**

```bash
git reset --hard eb3dffa
# Working directory reset to Commit 2 state, Commit 3 is gone.
```

> ⚠️ Be very careful with `--hard`! Changes are **permanently deleted locally**.

---

## Part B: `git revert` (Safe Undo)

`git revert` **does not delete history**. Instead, it creates a **new commit** that undoes the changes of a previous commit.

### Step-by-Step `git revert`

Undo **Commit 3** (`8e28244`) safely:

```bash
git revert 8e28244
```

1. **Editor Opens:** Git prompts for a **Revert Commit message**. You can keep the default message. Save & close.
2. **New Commit:** A new commit appears that **reverses Commit 3**, while the original commit **remains in history**.

**Example Log After Revert:**

```
[NEW_SHA] Revert "Commit 3: Added file C"  <-- New Revert Commit
8e28244 (HEAD -> main) Commit 3: Added file C <-- Original Commit 3 still exists
eb3dffa Commit 2: Added file B
...
```

✅ `git revert` is **safe for public branches** and collaboration since it **does not rewrite history**.

---

# 🚀 Challenge 5: Amend the Last Commit (`git commit --amend`)

`git commit --amend` is a **powerful command** that lets you **edit the last commit** without creating a new commit in history. You can **change the commit message** and **add forgotten files**.

---

## 🎯 Goal

1. **Edit** the message of the last commit (`f3cc90d` - Revert "deleting it").
2. **Add** a new file or changes to that same commit.

---

## Step 1: Prepare the File (Add Forgotten File)

First, create a **new file** or **modify an existing one** that you forgot to include in the last commit.

```bash
# Create a new file
echo "forgotten content" > forgotten_file.txt

# Stage the new or modified file
git add forgotten_file.txt
```

---

## Step 2: Amend the Commit

Now, use the `--amend` flag to **combine staged changes with the last commit**.

```bash
# Amend the last commit
git commit --amend
```

---

## Step 3: Edit the Commit Message

1. Your **editor opens** showing the previous commit message (e.g., `Revert "deleting it"`).
2. Replace it with a **new message**, for example:

   ```
   Final cleanup and included forgotten file
   ```
3. **Save and close** the editor.

---

## 🎊 Result

* **History:** Git **replaces the previous commit** with a new one.
* **Commit Count:** The number of commits stays the same; only the **SHA of the last commit changes**.
* **Content:** The last commit now includes **both the new file** (`forgotten_file.txt`) and the **updated commit message**.

---

## Alternative: Amend Only the Message

If you want to **change only the commit message** without adding files, use the `-m` or `--no-edit` flag.

```bash
# Only change the message, no new files
git commit --amend -m "This is the completely new message"
```

> ✅ The editor will not open, and the message changes directly.


---



## Challenge 6: Git Pre-Commit Hook – Step-by-Step

### 🎯 Goal

Create a **pre-commit hook** that **prevents committing** if the `README.md` file does **not** contain a specific line (`[FINAL REVIEW DONE]`). This automates a quality check before committing code.

---

### Step 1: Locate the Hooks Directory

Git hooks live in `.git/hooks` inside your repository. These are executable scripts that Git runs at specific points (like `pre-commit`, `post-commit`, etc.).

```bash
cd .git/hooks
ls
# You will see files like pre-commit.sample, post-commit.sample, etc.
```

> ✅ Tip: Hooks are **local only** and do not get pushed to remote repositories by default.

---

### Step 2: Create the `pre-commit` Script

Create a **new file** named `pre-commit` (no extension):

```bash
nano pre-commit
```

**Paste this script:**

```bash
#!/bin/sh

# Find the root directory of the Git repository
REPO_ROOT=$(git rev-parse --show-toplevel)

# File and required text to check
FILE_TO_CHECK="README.md"
REQUIRED_TEXT="[FINAL REVIEW DONE]"

# Check if the required text exists
if ! grep -q "$REQUIRED_TEXT" "$REPO_ROOT/$FILE_TO_CHECK"; then
    echo "--------------------------------------------------------"
    echo "🚨 COMMIT FAILED: Pre-commit Hook Check"
    echo "The file $FILE_TO_CHECK MUST contain the line: '$REQUIRED_TEXT'"
    echo "Please add the required review tag and try committing again."
    echo "--------------------------------------------------------"
    exit 1
fi

exit 0
```

**What this does:**

* `#!/bin/sh`: Uses the standard shell to run the script.
* `git rev-parse --show-toplevel`: Finds the root directory of the repository.
* `grep -q`: Quietly checks if the required text exists.
* `exit 1`: Stops the commit if the text is missing.
* `exit 0`: Allows the commit if the check passes.

---

### Step 3: Make the Script Executable

```bash
chmod +x pre-commit
```

> Without `+x`, Git will **ignore** the hook.

---

### Step 4: Test the Hook – Failure Scenario

Try committing **without the required text**:

```bash
echo "Some temp change" >> temp_file.txt
git add temp_file.txt
git commit -m "Testing hook failure"
```

**Expected Output:**

```
--------------------------------------------------------
🚨 COMMIT FAILED: Pre-commit Hook Check
The file README.md MUST contain the line: '[FINAL REVIEW DONE]'
Please add the required review tag and try committing again.
--------------------------------------------------------
```

> The commit is blocked. ✅

---

### Step 5: Test the Hook – Success Scenario

Now, satisfy the condition:

```bash
echo "[FINAL REVIEW DONE]" >> README.md
git add README.md temp_file.txt
git commit -m "Testing hook success"
```

**Expected Output:**

```
[main <NEW_SHA>] Testing hook success
 2 files changed, 2 insertions(+)
 create mode 100644 temp_file.txt
```

> The commit succeeds because the required text exists.

---

### Step 6: Key Takeaways

| Feature             | Benefit                                                                                   |
| ------------------- | ----------------------------------------------------------------------------------------- |
| Pre-commit hook     | Automates checks **before committing**. Prevents bad commits.                             |
| `grep` check        | Ensures required lines or patterns exist in files.                                        |
| `exit 1` / `exit 0` | Controls whether the commit **fails or succeeds**.                                        |
| Local only          | Hooks **don’t travel** with the repo unless explicitly shared (via scripts or templates). |

---


## Challenge 7: Rebase a Feature Branch on Main

### 🎯 Goal

Move all commits from `git-adv-practice` branch to sit **on top of the latest `main` commits**, keeping history **linear** and **avoiding unnecessary merge commits**.

---

### Step 1: Update the Main Branch

Make sure your local `main` is fully synced with the remote:

```bash
# Switch to main branch
git checkout main

# Pull latest changes from remote
git pull origin main
```

* If it says `Already up to date`, your branch is current.
* Otherwise, your `main` branch now includes all latest commits from remote.

---

### Step 2: Rebase the Feature Branch

Switch to your feature branch and start the rebase:

```bash
# Switch to feature branch
git checkout git-adv-practice

# Rebase it on top of main
git rebase main
```

**What this does:**

* Temporarily moves your `git-adv-practice` commits aside.
* Updates your branch with all latest commits from `main`.
* Reapplies your feature branch commits **on top** of main’s latest commit.

---

### Step 3: Handle Conflicts (If Any)

Conflicts may appear if both branches changed the same files. Git will show something like:

```
CONFLICT (content): Merge conflict in README.md
error: could not apply [Commit ID]...
```

**Resolve conflicts step-by-step:**

1. **Edit conflicted files**
   Remove conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`) and finalize code.

2. **Stage resolved files**

```bash
git add README.md
```

3. **Continue the rebase**

```bash
git rebase --continue
```

4. Repeat for any other conflicts until rebase completes:

```
Successfully rebased and updated refs/heads/git-adv-practice
```

> ⚠️ Optional: Abort rebase if needed:

```bash
git rebase --abort
```

---

### Step 4: Merge the Rebased Feature Branch into Main

Once the rebase is successful, do a **fast-forward merge**:

```bash
# Switch to main
git checkout main

# Merge the rebased branch (fast-forward)
git merge git-adv-practice
```

**Result:**

* No new merge commit is created.
* `main` now points directly to the latest commit from `git-adv-practice`.

---

### Step 5: Push Changes to Remote

Finally, push the clean, linear history to GitHub:

```bash
git push origin main
```

---

### ✅ Summary

| Action              | Benefit                                                                    |
| ------------------- | -------------------------------------------------------------------------- |
| `git rebase main`   | Applies feature commits on top of latest main, keeping history **linear**. |
| Conflict resolution | Ensures merged code is correct **before finalizing**.                      |
| Fast-forward merge  | Avoids unnecessary merge commits, keeping Git history clean.               |
| Push                | Share the clean branch history with your team.                             |

---


# 🚀 Challenge 8: Squash Multiple Commits into One (`git rebase -i`)

Sometimes, you make **multiple small commits** on a feature branch, but you want to **clean up history** before merging into `main`. This is where **interactive rebase** and **squashing commits** come in.

---

## 🎯 Goal

* Create a branch, make multiple commits.
* Combine (squash) all commits into **one single commit** to keep history **clean and readable**.

---

## Step 1: Create a New Branch and Make Multiple Commits

```bash
# Create a new branch
git checkout -b feature-squash-demo

# Commit 1
echo "Line 1" > demo.txt
git add demo.txt
git commit -m "Add Line 1"

# Commit 2
echo "Line 2" >> demo.txt
git add demo.txt
git commit -m "Add Line 2"

# Commit 3
echo "Line 3" >> demo.txt
git add demo.txt
git commit -m "Add Line 3"
```

> ✅ You now have **3 commits** in `feature-squash-demo`.

---

## Step 2: Start Interactive Rebase

Use **interactive rebase** to squash commits into one.

```bash
# Start interactive rebase for last 3 commits
git rebase -i HEAD~3
```

* `HEAD~3` → Last 3 commits.
* Git will open an **editor** showing:

```
pick abc123 Add Line 1
pick def456 Add Line 2
pick ghi789 Add Line 3
```

---

## Step 3: Squash Commits

1. Leave the **first commit** as `pick`.
2. Change the next commits to `squash` (or `s`):

```
pick abc123 Add Line 1
squash def456 Add Line 2
squash ghi789 Add Line 3
```

3. Save and close the editor.

> This tells Git: **combine the second and third commits into the first commit**.

---

## Step 4: Edit Commit Message

Git will now prompt you to **edit the commit message** for the combined commit:

```
# This is a combination of 3 commits.
# The first commit's message is:
Add Line 1

# The following commit messages will be included:
Add Line 2
Add Line 3
```

* Edit the message to something concise, e.g.:

```
Add demo.txt with 3 lines
```

* Save and close the editor.

---

## Step 5: Verify the History

```bash
git log --oneline
```

**Expected Output:**

```
<NEW_SHA> Add demo.txt with 3 lines  <-- Single squashed commit
```

> ✅ All 3 commits are now **squashed into one clean commit**.

---

## Step 6: Merge Squashed Branch into Main

After squashing, merge into `main`:

```bash
# Switch to main
git checkout main

# Merge the squashed branch (fast-forward)
git merge feature-squash-demo
```

> No extra merge commits are created. History stays **linear and clean**.

---

## ✅ Key Notes

1. **Interactive Rebase (`-i`)** is safe for **local/private branches**.
2. **Never squash commits that are already pushed** to a public/shared branch unless you coordinate with teammates.
3. **Commit message** should summarize all combined changes.
4. This workflow is **excellent for feature branches** before merging into main.

---

## ⏭️ Next Step
👉 Tomorrow’s focus: **Day 05 –  Python Basics for DevOps**
---
📌 Resource: [ **Day 05 –  Python Basics for DevOps**](https://www.learnxops.com/python-basics-for-devops/)