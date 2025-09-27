
# 🚀 99 Days of DevOps Challenge  

**Day 05 – Python Basics for DevOps**  

---

## 🌍 Introduction  

Python is one of the most important languages in DevOps. It is widely used for **automation, infrastructure as code, monitoring, CI/CD, and cloud scripting**.  

* **What** → Python is a high-level, interpreted programming language.  
* **Why** → Easy to learn, has powerful libraries, great for automation.  
* **When** → Whenever automating tasks, handling files, APIs, or server management.  
* **Where** → Used in Ansible, AWS Boto3 SDK, Kubernetes client libraries, monitoring tools.  
* **How** → By writing Python scripts that integrate with OS commands, APIs, and cloud services.  

👉 In DevOps, **Python = Automation Superpower ⚡**  

---

## 📖 Key Learnings  

* Learned **variables, functions, file handling, loops, and modules** in Python.  
* Used Python for **automation, monitoring, API calls, and OS-level tasks**.  
* Practiced real-world challenges that reflect **DevOps workflows**.  

---

## ✅ Challenges & Solutions  

#### 🔹 Challenge 1: Create a Python program that accepts a user’s name as input and prints a greeting message.  

```python
# -------------------
# Challenge 01
# -------------------
print("Challenge-01")
name = input("Enter your name :")  # Take user input
print(f"Welcome back {name}")      # Print greeting message
````

📌 **Explanation**:
We used `input()` to take user input and **f-strings** (`f"..."`) to format the output.

---

#### 🔹 Challenge 2: Write a script that reads a text file and counts the number of words in it.

```python
# -------------------
# Challenge 02
# -------------------
with open("read.txt", "r") as file:
    # Read the content of the file
    file_content = file.read()
    print(file_content)
    
    # Split the content into words
    word_list = file_content.split()
    print(word_list)
    
    # Count the number of words
    word_count = len(word_list)
    print("Total number of words in the file:")
    print(word_count)
```

📌 **Explanation**:
We opened a file with `with open()`. Used `.split()` to break content into words, then used `len()` to count.

---

#### 🔹 Challenge 3: Create a Python script that generates a random password of 12 characters.

```python
# -------------------
# Challenge 03
# -------------------
import random
import string  # Provides letters, digits, and punctuation sets

password = ""              # Empty string initially
password_length = 12       # Desired password length

# All possible characters (letters + digits + symbols)
characters = string.ascii_letters + string.digits + string.punctuation

# Generate random password
for i in range(password_length):
    random_char = random.choice(characters)  # Pick random character
    password += random_char                  # Add to password

print(password)  # Print final password
```

📌 **Explanation**:
We used `random.choice()` with `string` library sets to generate secure passwords.

---

#### 🔹 Challenge 4: Implement a Python program that checks if a number is prime.

```python
# -------------------
# Challenge 04
# -------------------
def is_prime(num):
    if num <= 1:
        return False
    
    for i in range(2, num):
        if num % i == 0: 
            return False
        else:
            return True

print(is_prime(11))  # True
print(is_prime(4))   # False
```

📌 **Explanation**:
We used loops and modulus (`%`) operator. If divisible by any number → not prime.

---

#### 🔹 Challenge 5: Write a script that reads a list of server names from a file and pings each one.

```python
# -------------------
# Challenge 05
# -------------------
import subprocess
import platform

SERVER_FILE = "server_list.txt" 

def get_ping_command():
    if platform.system().lower() == "windows":
        return ["ping", "-n", "1"]
    else:
        return ["ping", "-c", "1"]

def ping_servers_from_file(file_path):
    try:
        with open(file_path, 'r') as f:
            server_names = [line.strip() for line in f if line.strip()]
        
        base_ping_command = get_ping_command()
        
        for server in server_names:
            print(f"\n[ PINGING ] -> {server}")
            full_command = base_ping_command + [server]
            
            result = subprocess.run(full_command, capture_output=True, text=True, timeout=5)
            
            if result.returncode == 0:
                print("Status: SUCCESS (Connected)")
            else:
                print("Status: FAILED (Unreachable)")
                
    except FileNotFoundError:
        print(f"ERROR: File '{file_path}' not found.")

if __name__ == "__main__":
    ping_servers_from_file(SERVER_FILE)
```

📌 **Explanation**:
We used `subprocess.run()` to execute OS-level `ping` commands. File `server_list.txt` should contain server names (one per line).

---

#### 🔹 Challenge 6: Use the requests module to fetch and display data from a public API.

```python
# -------------------
# Challenge 06
# -------------------
import requests
import json

base_url = "https://jsonplaceholder.typicode.com"

def fetch_data(endpoint):
    url = f"{base_url}/{endpoint}"
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        data = response.json()
        print(json.dumps(data, indent=3)[:600] + "...")
    else:
        print(f"FAILED: {response.status_code}")

if __name__ == "__main__":
    fetch_data("posts/1")
    fetch_data("users")
```

📌 **Explanation**:
We fetched data using `requests.get()`. Converted JSON to readable format using `json.dumps()`.

---

#### 🔹 Challenge 7: Automate a simple task using Python (Renaming multiple files).

```python
# -------------------
# Challenge 07
# -------------------
import os

TARGET_DIR = "."
TARGET_EXTENSION = ".txt"
NEW_PREFIX = "processed_"

def rename_files(directory, extension, prefix):
    file_list = os.listdir(directory)
    for filename in file_list:
        old_path = os.path.join(directory, filename)
        if os.path.isfile(old_path) and filename.endswith(extension):
            if filename.startswith(prefix):
                continue
            new_filename = prefix + filename
            new_path = os.path.join(directory, new_filename)
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_filename}")

rename_files(TARGET_DIR, TARGET_EXTENSION, NEW_PREFIX)
```

📌 **Explanation**:
We used `os.listdir()` to list files and `os.rename()` to rename them with a new prefix.

---

#### 🔹 Challenge 8: Create a Python script that monitors CPU and memory usage every 5 seconds.

```python
# -------------------
# Challenge 08
# -------------------
import psutil
import time
import datetime

def monitor_system():
    while True:
        cpu_usage = psutil.cpu_percent(interval=None)
        memory_stats = psutil.virtual_memory()
        mem_percent = memory_stats.percent
        mem_used_gb = memory_stats.used / (1024 ** 3)

        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"{current_time} | CPU: {cpu_usage}% | Memory: {mem_percent}% | Used: {mem_used_gb:.2f} GB")
        
        time.sleep(5)

if __name__ == "__main__":
    monitor_system()
```

📌 **Explanation**:
We used `psutil` to get CPU & memory stats. `time.sleep(5)` repeats monitoring every 5 seconds.

---

#### 🔹 Challenge 9: Write a Python program that creates a user in Linux using subprocess and verifies the creation.

```python
# -------------------
# Challenge 09
# -------------------
import subprocess
import sys

def create_and_verify_user(username):
    create_cmd = ["sudo", "useradd", "-m", username]
    creation_result = subprocess.run(create_cmd, capture_output=True, text=True)

    if creation_result.returncode == 0:
        print(f"User '{username}' created successfully.")
    else:
        print(f"FAILED: {creation_result.stderr.strip()}")
        return
    
    verify_cmd = ["id", username]
    verification_result = subprocess.run(verify_cmd, capture_output=True, text=True)

    if verification_result.returncode == 0:
        print(f"Verification Success:\n{verification_result.stdout.strip()}")
    else:
        print(f"Verification FAILED for user {username}.")

if __name__ == "__main__":
    new_user = "devops_intern"
    print("Run with: sudo python3 script.py")
    create_and_verify_user(new_user)
```

📌 **Explanation**:
We used `subprocess.run()` to execute Linux commands: `useradd` to create users and `id` to verify. Requires **sudo/root privileges**.

---

✨ Day 5 done! Consistency is 🔑

---

## ⏭️ Next Step

👉 Tomorrow’s focus: **Day 06 – Advanced Python for Devops**
📌 Link: [Next Challenge](https://www.learnxops.com/advanced-python-for-devops/)

---

