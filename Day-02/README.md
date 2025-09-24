
# 🚀 99 Days of DevOps Challenge
 
**Day 02 – Linux Shell Scripting & Automation**

# 🐚 Shell Scripting - DevOps Challenges

## 📌 What is a Shell Script?
A **Shell Script** is a text file that contains a series of commands for a Unix/Linux shell to execute.  
It helps automate repetitive tasks, system monitoring, and software management.

---

## 🤔 Why Use Shell Scripts?
- Automates repetitive manual work  
- Saves time and reduces errors  
- Useful for system administration, DevOps, and CI/CD pipelines  
- Can combine multiple Linux commands into one workflow  

---

## ⏳ When to Use Shell Scripts?
- Daily system monitoring (CPU, memory, logs)  
- File management (backups, cleanups)  
- User account automation  
- Deployments & server setup  
- Cron jobs (scheduled tasks)  

---

## ✅ Advantages
- Easy to learn and write  
- Fast automation of tasks  
- Portable across Unix/Linux systems  
- Can integrate with other tools (cron, awk, sed, etc.)  

---

## ⚠️ Disadvantages
- Slower than compiled languages (C, Go, Rust)  
- Error handling is limited  
- Not secure if written poorly (e.g., storing passwords in scripts)  
- Harder to maintain for very large projects  

---

# 🚀 Challenges & Solutions

---

### 🔹 Challenge 1: Print “Hello DevOps” with Current Date & Time
```bash
####################
# Name : Mohammed Yasir Khan
# Date : 24/09/2025
# Description : Prints “Hello DevOps” with the current date and time.
##################
#!/bin/bash
todays_date=$(date)
echo "Hello DevOps $todays_date"
````

---

### 🔹 Challenge 2: Create a script that checks if a website (e.g., https://www.learnxops.com) is reachable using curl or ping. Print a success or failure message.

**Verbose Solution using curl + ping**

```bash
####################
# Name : Mohammed Yasir Khan
# Date : 24/09/2025
# Description : Check if a Website is Reachable.
##################
#!/bin/bash

WEBSITE="https://www.learnxops.com"
DOMAIN="learnxops.com"

if curl -Is "$WEBSITE" --max-time 5 | head -n 1 | grep -q "200\|301\|302"; then
    echo "✅ Success: $WEBSITE is reachable via curl!"
else
    echo "⚠️ Curl check failed, trying ping..."

    if ping -c 2 -W 2 "$DOMAIN" > /dev/null 2>&1; then
        echo "✅ Success: $DOMAIN is reachable via ping!"
    else
        echo "❌ Failure: $WEBSITE is not reachable via curl or ping."
    fi
fi
```

---

### 🔹 Challenge 3: Write a script that takes a filename as an argument, checks if it exists, and prints the content of the file accordingly.

```bash
####################
# Name : Mohammed Yasir Khan
# Date : 24/09/2025
# Description : Check if a File Exists & Print Content.
##################
#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <filename>"
    exit 1
fi

file="$1"

if [ -f "$file" ]; then
    echo "File '$file' exists. Content:"
    echo "--------------------------"
    cat "$file"
else
    echo "Error: File '$file' does not exist or is not a regular file."
fi
```

---

### 🔹 Challenge 4: Save Running Processes to File

```bash
####################
# Name : Mohammed Yasir Khan
# Date : 24/09/2025
# Description : Save Running Processes to File
##################
#!/bin/bash
ps -aux > process_list.txt 2>&1
```

---

### 🔹 Challenge 5:Write a script that installs multiple packages at once (e.g., git, vim, curl). The script should check if each package is already installed before attempting installation.

```bash
####################
# Name : Mohammed Yasir Khan
# Date : 24/09/2025
# Description : Install Multiple Packages (if not installed)
##################
#!/bin/bash

PACKAGES=("git" "vim" "curl")

echo "Starting package installation check..."
echo "------------------------------------"

for package in "${PACKAGES[@]}"; do
    echo "Checking for package: $package..."

    if dpkg-query -W --showformat='${Status}\n' "$package" 2>/dev/null | grep -q "install ok installed"; then
        echo "$package is already installed. Skipping."
    else
        echo "$package is not installed. Installing..."
        sudo apt-get install -y "$package"
        
        if [ $? -eq 0 ]; then
            echo "$package installed successfully."
        else
            echo "Failed to install $package."
        fi
    fi
    echo ""
done

echo "------------------------------------"
echo "Package installation check complete."
```

---

### 🔹 Challenge 6:  Create a script that monitors CPU and memory usage every 5 seconds and logs the results to a file.

```bash
####################
# Name : Mohammed Yasir Khan
# Date : 24/09/2025
# Description : script that monitors CPU and memory usage every 5 seconds and logs the results to a file.
##################
#!/bin/bash

LOG_FILE="resource_log.txt"
INTERVAL=5

echo "Starting resource monitoring. Press Ctrl+C to stop."
echo "Monitoring started at $(date)" > "$LOG_FILE"
echo "---------------------------------------------------" >> "$LOG_FILE"

while true; do
  TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
  CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')
  MEM_USAGE=$(free | grep "Mem" | awk '{print ($3/$2) * 100.0}')
  
  echo "[$TIMESTAMP] CPU: $CPU_USAGE% | Mem: $MEM_USAGE%" >> "$LOG_FILE"
  sleep "$INTERVAL"
done
```

---

### 🔹 Challenge 7: Write a script that automatically deletes log files older than 7 days from /var/log.

```bash
####################
# Name : Mohammed Yasir Khan
# Date : 24/09/2025
# Description : script that automatically deletes log files older than 7 days from /var/log.
##################
#!/bin/bash

LOG_DIR="/var/log"
DAYS_OLD=7

echo "Starting log cleanup in $LOG_DIR..."
find "$LOG_DIR" -type f -name "*.log" -mtime +$DAYS_OLD -exec echo "Deleting: {}" \; -delete
echo "Cleanup complete."
```

---

### 🔹 Challenge 8: Automate user account creation – Write a script that takes the username as an argument, checks, if the user exists, gives the message “user already exists“ else creates a new user, adds it to a “devops“ group, and sets up a default home directory.

```bash
####################
# Name : Mohammed Yasir Khan
# Date : 24/09/2025
# Description : Automate user account creation 
##################
#!/bin/bash

if [ -z "$1" ]; then
    echo "Error: Please provide a username as an argument."
    echo "Usage: sudo $0 <username>"
    exit 1
fi

USERNAME="$1"

if id -u "$USERNAME" &>/dev/null; then
    echo "Error: User '$USERNAME' already exists."
    exit 1
fi

echo "User '$USERNAME' does not exist. Creating..."

groupadd devops 2>/dev/null || true

useradd -m -s /bin/bash -g devops "$USERNAME"

if [ $? -eq 0 ]; then
    echo "✅ Success: User '$USERNAME' created and added to the 'devops' group."
    echo "Home directory: /home/$USERNAME"
else
    echo "❌ Failure: Failed to create user '$USERNAME'."
    exit 1
fi

echo "To set a password for the new user, run: sudo passwd $USERNAME"
```

---

### 🔹 Challenge 9: Use awk or sed in a script to process a log file and extract only error messages.

```bash
####################
# Name : Mohammed Yasir Khan
# Date : 24/09/2025
# Description : IExtract Error Logs using `sed`
##################
#!/bin/bash

LOG_FILE="application.log"
ERROR_FILE="errors.log"

if [ ! -f "$LOG_FILE" ]; then
  echo "Error: Log file '$LOG_FILE' not found."
  exit 1
fi

echo "Extracting error messages from $LOG_FILE..."
sed -n '/ERROR/p' "$LOG_FILE" > "$ERROR_FILE"
echo "Done. Error messages saved to $ERROR_FILE."
```
OR  (using awk)
```bash
# Name : Mohammed Yasir Khan
# Date : 24/09/2025
# Description : IExtract Error Logs using `awk`
##################
#!/bin/bash

LOG_FILE="application.log"
ERROR_FILE="errors.log"

# Check if the log file exists
if [ ! -f "$LOG_FILE" ]; then
  echo "Error: Log file '$LOG_FILE' not found."
  exit 1
fi

echo "Extracting error messages from $LOG_FILE..."

# Use awk to find lines with the word "ERROR" and save them to a file
awk '/ERROR/ {print}' "$LOG_FILE" > "$ERROR_FILE"

echo "Done. Error messages saved to $ERROR_FILE."
```

---

### 🔹Challenge 10: Set up a cron job that runs a script to back up (zip/tar) a directory daily.

```bash
####################
# Name : Mohammed Yasir Khan
# Date : 24/09/2025
# Description : Backup Directory with Cron
##################
#!/bin/bash

SOURCE_DIR="/home/user/my_projects"
BACKUP_DIR="/var/backups"
DATE=$(date +%Y-%m-%d)
BACKUP_FILE="$BACKUP_DIR/my_projects-$DATE.tar.gz"

if [ ! -d "$BACKUP_DIR" ]; then
    mkdir -p "$BACKUP_DIR"
fi

tar -czf "$BACKUP_FILE" "$SOURCE_DIR"
echo "Backup of $SOURCE_DIR to $BACKUP_FILE completed successfully."
```

---

## 🕒 Setting up the Backup Cron Job

Run `crontab -e` and add:

```
0 2 * * * /path/to/backup_script.sh
```

👉 This runs the backup every day at **2 AM**.

---

## 📖 Conclusion

* Shell scripts are **powerful automation tools** for DevOps.
* These 10 challenges cover **basics of scripting, automation, monitoring, and system administration**.
* Keep practicing and combining these small scripts to build **real-world automation projects**.

---


## ⏭️ Next Step
👉 Tomorrow’s focus: **Day 03 – Linux Shell Scripting & Automation**
📌 Resource: [Day 3: Git & GitHub - Basics, Branching, Merging, PRs](https://www.learnxops.com/git-github-basics-branching-merging-prs-challange/)