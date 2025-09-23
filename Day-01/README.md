
# 🚀 99 Days of DevOps Challenge

**Day 01 – Linux Basics (Commands, File System, Users & Permissions)**

---

## 🌍 Introduction

Linux is the backbone of almost every cloud platform, container, and DevOps tool.

* **What** → Linux is an open-source operating system widely used in servers and cloud.
* **Why** → It’s stable, secure, lightweight, and provides strong CLI-based control.
* **When** → Whenever managing servers, containers, or deploying applications.
* **Where** → Used in AWS, Kubernetes nodes, Docker containers, Android OS, and networking devices.
* **How** → Through shell commands, scripting, and automation.

👉 In DevOps, **Linux = Control Center**.

---

## 📖 Key Learnings

* Navigated Linux file system using shell commands.
* Explored the Linux directory structure (`/etc`, `/var`, `/home`).
* Learned about file permissions (`chmod`, `chown`, `rwx`).
* Created and managed users & groups.
* Practiced real-world challenges to strengthen fundamentals.

---

## 📝 Commands & Examples

| Command                    | Description                          | Example Output                             |
| -------------------------- | ------------------------------------ | ------------------------------------------ |
| `pwd`                      | Print working directory              | `/home/ubuntu`                             |
| `ls -la`                   | List all files including hidden ones | `drwxr-xr-x  2 user user 4096 Sep 23 .`    |
| `mkdir devops`             | Create a new directory               | *(creates a folder named devops)*          |
| `chmod 600 file.txt`       | Give owner read/write only           | `-rw------- 1 user user 0 Sep 23 file.txt` |
| `sudo adduser devops_user` | Add a new user                       | *(prompts for password setup)*             |

---

## ✅ Challenges & Solutions 
#### (Note: I am completing the challenge on an EC2 instance as the ubuntu user. Therefore, I used sudo to gain temporary root privileges when required. If you are logged in as the root user, you don’t need to use sudo.)

### 🔹 Challenge 1: List all files (including hidden ones) in home directory and sort by modification time

```bash
ls -lta ~
```
![List all files: ](/Day-01/screenshots/output-01.png)
---

### 🔹 Challenge 2: Create a directory and file

```bash
mkdir devops_challenge_day_1
cd devops_challenge_day_1
touch day1.txt
```
![Create a directory and file:  ](/Day-01/screenshots/output-02.png)
---

### 🔹 Challenge 3: Find total disk usage of `/var/log`

```bash
sudo du -sh /var/log
```
![total disk usage of /var/log:  ](/Day-01/screenshots/output-03.png)

---

### 🔹 Challenge 4: Create a new user and add to sudo group

```bash
sudo adduser devops_user
cat /etc/passwd  #verify user is created or not
sudo usermod -aG sudo devops_user
cat /etc/group #to check user group
id devops_user  #best approach, tells userid, groupid, and groups where user is part of it
```

* OR 

```bash
sudo useradd -m -s /bin/bash devops_user
sudo passwd devops_user
sudo usermod -aG sudo devops_user
id devops_user
```
![Create a new user and add to sudo group: ](/Day-01/screenshots/output-04.png)
![](/Day-01/screenshots/output-05.png)

---

### 🔹 Challenge 5: Create group and add user

```bash
sudo groupadd devops_team
sudo usermod -aG devops_team devops_user
groups devops_user
```
![Create group and add user: ](/Day-01/screenshots/output-05.png)

---

### 🔹 Challenge 6: Set permissions on `day1.txt` (owner = read/write only)

```bash
chmod 600 day1.txt
ls -ltra day1.txt
```
![Set permissions on `day1.txt`: ](/Day-01/screenshots/output-06.png)

---

### 🔹 Challenge 7: Find files in `/etc` modified in last 7 days

```bash
find /etc -type f -mtime -7
```
![Find files in `/etc` modified in last 7 days: ](/Day-01/screenshots/outout-07.png)


---

### 🔹 Challenge 8: Find most frequently used command in history

```bash
history | awk '{CMD[$2]++} END {for (a in CMD) print CMD[a], a}' | sort -nr | head -1
```
![Find most frequently used command in history: ](/Day-01/screenshots/outout-08.png)

---


* Got comfortable with Linux navigation and commands.
* Learned **why permissions are crucial** in multi-user systems.
* Practiced **user & group management** which is key in DevOps environments.
* These fundamentals will help in automation, server management, and security.

---

## 📂 Repo Structure

```
99-days-devops-challenge/
 ├── Day01_Linux_Basics/
 │   ├── README.md   # Notes + challenges
 │   ├── screenshots # Terminal outputs
     
 ```

✨ Day 1 done! Consistency is key 🚀

## ⏭️ Next Step
👉 Tomorrow’s focus: **Day 02 – Linux Shell Scripting & Automation**
📌 Resource: [Linux Shell Scripting Challenge](https://www.learnxops.com/linux-shell-scripting-automation-challenge)

---




