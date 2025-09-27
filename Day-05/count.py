# -------------------
# challenge 01
# ------------------
# print("Challenge-01")
# name = input("Enter your name :")
# print(f"Welcome back {name}")

# -------------------
# challenge-02
# -------------------
# with open("read.txt", "r") as file:
#     # Read the content of the file
#     file_content= file.read()
#     print(file_content)
    
#     # Split the content into words
#     word_list = file_content.split()
#     print(word_list)
    
#     # Count the number of words
#     word_count = len(word_list)
#     print("Total number of words in the file:")
    # print(word_count)

# -------------------
# challenge-03
# -------------------

# # Generate a random words
# import random
# # importing string module ......(letters, digits, symbols ke built-in sets)
# import string

# # Initallily empty password string
# password = ""

# # Length of the password
# password_length = 12

# # All possible characters that can be used in the password
# characters = string.ascii_letters
# # adding all possible numbers to the characters string with possible characters
# characters += string.digits
# # adding all possible punctuation to the characters string with alphabets + digits
# characters += string.punctuation

# # Generating a random password
# for i in range(password_length):
#     # Choosing a random character from the characters string
#     random_char = random.choice(characters)

#     # Appending the random character to the password string
#     password += random_char

# # Printing the generated password
# print(password)


# # -------------------
# # Challenge 4: Implement a Python program that checks if a number is prime.
# # -------------------

# def is_prime(num):
#     if num<=1:
#         return False
    
#     for i in range(2, num):

#         if num % i == 0 : 
#             return False
        
#         else:
#             return True
        
    
# print(is_prime(11))  # True
# print(is_prime(4))   # False



# # Challenge 5: Write a script that reads a list of server names from a file and pings each one.

# import subprocess
# import platform
# import sys

# # Define the file path where server names are listed (one per line)
# SERVER_FILE = "server_list.txt" 
# def get_ping_command():
#     """
#     Operating System ke hisaab se correct 'ping' command return karta hai.
#     Windows aur Unix-like systems (Linux/macOS) ke ping options alag hote hain (e.g., -n vs -c).
#     """
#     # Check karta hai ki hum Windows par hain ya nahi
#     if platform.system().lower() == "windows":
#         # Windows mein '-n 1' ka matlab hai 1 packet bhejo
#         return ["ping", "-n", "1"]
#     else:
#         # Linux/macOS mein '-c 1' ka matlab hai 1 packet bhejo
#         return ["ping", "-c", "1"]

# def ping_servers_from_file(file_path):
#     """
#     Diye gaye file se server names read karta hai aur har server ko ping karta hai.
#     """
#     print(f"--- Starting Ping Test from file: {file_path} ---")
    
#     try:
#         # 'with open' se file automatically close ho jaati hai, best practice hai
#         with open(file_path, 'r') as f:
#             # Lines ko read karo aur server names ki list banao
#             server_names = [line.strip() for line in f if line.strip()]

#         # Agar list empty hai, toh ruk jao
#         if not server_names:
#             print("ERROR: File is empty or contains no server names.")
#             return

#         # OS specific ping command le lo
#         base_ping_command = get_ping_command()
        
#         # Har server name ko loop karo
#         for server in server_names:
#             print(f"\n[ PINGING ] -> {server}")
            
#             # Final command banao (e.g., ['ping', '-c', '1', 'google.com'])
#             full_command = base_ping_command + [server]
            
#             try:
#                 # subprocess.run() OS command execute karta hai
#                 # capture_output=True se output ko store kar sakte hain
#                 # text=True se output string format mein milta hai
#                 result = subprocess.run(
#                     full_command, 
#                     capture_output=True, 
#                     text=True,
#                     timeout=5 # 5 seconds ke baad ruk jayega agar server slow hai
#                 )
                
#                 # Check karo ki ping successful hua ya nahi (return code 0)
#                 if result.returncode == 0:
#                     print("Status: SUCCESS (Connected)")
#                     # Ping ka main output print karo (agar zaroori ho)
#                     # print("Output:\n" + result.stdout.strip().split('\n')[-2])
#                 else:
#                     print("Status: FAILED (Server unreachable or command error)")
#                     # Agar failed, toh error print karo
#                     # print("Error:\n" + result.stderr.strip())

#             except subprocess.TimeoutExpired:
#                 print("Status: TIMEOUT (Ping took too long)")
#             except FileNotFoundError:
#                 # Agar 'ping' command hi OS mein nahi mila
#                 print(f"Error: The 'ping' command was not found on your system.")
                
#     except FileNotFoundError:
#         print(f"ERROR: The file '{file_path}' was not found. Please create it.")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")

# # Script ko run karne ke liye
# if __name__ == "__main__":
#     # Ensure server_list.txt exists with some server names before running!
#     # e.g., google.com, 127.0.0.1, a-non-existent-server
    
#     # Example usage:
#     # 1. Create a file named 'server_list.txt'
#     # 2. Add server names, one per line (e.g., google.com, 127.0.0.1, badurl.xyz)
#     ping_servers_from_file(SERVER_FILE)


# import requests
# import json

# base_url = "https://jsonplaceholder.typicode.com"

# def fetch_data(endpoint):
#     try:
        
#         url = f"{base_url}/{endpoint}"
#         response = requests.get(url, timeout=10)

#         if response.status_code == 200:

#             data = response.json()
#             print("---------------------------")
#             print("Successfully fetched data.")
#             print("---------------------------")
#             print(f"Data Type: {type(data).__name__}")
#             # json.dumps() se hum data ko format karke (indent=2) readable way mein print karte hain
#             print(json.dumps(data, indent=3)[:600] + "...") # Sirf pehle 500 characters dikha rahe hain
            
#         elif response.status_code == 404:
#             print(f"Error 404: The endpoint '{endpoint}' was not found.")
#         else:
#             print(f"Status: FAILED ({response.status_code}) -> Kuch aur issue hai.")






#     except requests.exceptions.Timeout:
#         print("ERROR: Request timed out. Connection bahut slow hai.")
#     except requests.exceptions.ConnectionError:
#         print("ERROR: Connection fail ho gaya. Internet ya URL check karo.")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")


# if __name__ == "__main__":
#     # NOTE: Iss script ko chalaane se pehle, 'requests' library install karna zaroori hai:
#     # pip install requests
    
#     print("Starting Challenge 6: API Data Fetcher")
    
#     # --- Example 1: Single Resource Fetch karna (Ek specific post) ---
#     # Endpoint: 'posts/1'
#     fetch_data("posts/1")
    
#     # --- Example 2: List of Resources Fetch karna (Saare users ki list) ---
#     # Endpoint: 'users'
#     fetch_data("users")

#     # --- Example 3: Error Test (Endpoint jo exist nahi karta) ---
#     # Yeh 404 Not Found error dega
#     fetch_data("invalidendpoint123")








































# Challenge 8: Create a Python script that monitors CPU and memory usage every 5 seconds.

# import psutil
# import time
# import datetime # Timestamp ke liye

# def monitor_system():
#     """
#     Har 5 seconds mein CPU aur Memory usage check karta hai aur display karta hai.
#     """
#     print("-----------------------------------------------------------")
#     print("Timestamp | CPU Used(%) | Memory Used(%) | Memory Used(GB) |")
#     print("-----------------------------------------------------------")
    
#     # Loop ko humesha chalao jab tak user stop na kare
#     while True:
#         # 1. CPU Usage: psutil.cpu_percent() latest usage nikalta hai
#         # interval=None ka matlab hai ki yeh non-blocking call hai
#         cpu_usage = psutil.cpu_percent(interval=None) 
        
#         # 2. Memory Usage: virtual_memory() mein saari RAM stats hoti hain
#         memory_stats = psutil.virtual_memory()
#         mem_percent = memory_stats.percent # Percentage
        
#         # Bytes ko GB mein convert karo (1024 * 1024 * 1024)
#         mem_used_gb = memory_stats.used / (1024 ** 3) 
#         mem_total_gb = memory_stats.total / (1024 ** 3)

#         # 3. Timestamp
#         current_time = datetime.datetime.now().strftime("%H:%M:%S")

#         # 4. Data Display karo
#         # Output ko ek line mein clean tarike se format karo
#         print(
#             f"{current_time}  | "
#             f"{cpu_usage:12.1f} | "
#             f"{mem_percent:13.1f} | "
#             f"{mem_used_gb:15.2f} |"
#         )
        
#         # 5. 5 seconds ka wait
#         time.sleep(5)

# if __name__ == "__main__":
#     try:
#         print("System Monitor Started. (5-second interval)")
#         print("Press Ctrl+C to stop the monitoring.")
#         monitor_system()
#     except KeyboardInterrupt:
#         # Agar user Ctrl+C dabata hai, toh gracefully exit karo
#         print("\n---------------------------------------------------------")
#         print("Monitor Stopped by User. Task complete!")
#     except Exception as e:
#         print(f"\nAn unexpected error occurred: {e}")



# Challenge 7: Automate a simple task (Renaming multiple files).

# import os
# import sys

# # Woh directory jismein files hain. '.' ka matlab hai current directory.
# TARGET_DIR = "."
# # Woh extension jisko hum rename karna chahte hain
# TARGET_EXTENSION = ".txt"
# # Naya prefix jo files ke naam mein add hoga
# NEW_PREFIX = "processed_" 

# def rename_files(directory, extension, prefix):
#     """
#     Diye gaye directory mein specific extension wali files ko rename karta hai 
#     aur naya prefix add karta hai.
#     """
#     print(f"\n--- Starting to rename files in: {directory} ---")
    
#     try:
#         # 1. Directory ke andar ki saari cheezein nikaalo
#         file_list = os.listdir(directory)
#     except FileNotFoundError:
#         print(f"ERROR: Directory '{directory}' mili nahi.")
#         return
#     except Exception as e:
#         print(f"An error occurred while listing files: {e}")
#         return

#     renamed_count = 0
    
#     # 2. Har item par loop chalao
#     for filename in file_list:
#         # Puraana path banao (directory/filename)
#         old_path = os.path.join(directory, filename)
        
#         # 3. Check karo ki item file hai, aur extension match karta hai
#         # os.path.isfile check karta hai ki woh directory nahi hai
#         if os.path.isfile(old_path) and filename.endswith(extension):
            
#             # Agar file mein pehle se hi prefix hai, toh skip karo
#             if filename.startswith(prefix):
#                 print(f"Skipping: '{filename}' already has the prefix.")
#                 continue

#             # Naya file naam banao: (prefix + original_name)
#             new_filename = prefix + filename
#             new_path = os.path.join(directory, new_filename)
            
#             try:
#                 # 4. os.rename() se file ka naam badlo
#                 # Yeh sabse important line hai
#                 os.rename(old_path, new_path)
#                 print(f"Renamed: '{filename}' -> '{new_filename}'")
#                 renamed_count += 1
#             except Exception as e:
#                 print(f"ERROR renaming {filename}: {e}")

#     print(f"\n--- Renaming Complete. Total files renamed: {renamed_count} ---")


# if __name__ == "__main__":
#     # NOTE: Yeh script sirf tabhi files rename karega jab 'TARGET_DIR' mein 
#     # '.txt' files maujood hongi. Test karne ke liye kuch dummy files banao.
    
#     print("File Renamer Script Started.")
    
#     # 1. Tumhara pehla test: Current directory mein files rename karna
#     rename_files(TARGET_DIR, TARGET_EXTENSION, NEW_PREFIX)
    
#     # Example 2: Agar kisi doosri directory mein files rename karni hain
#     # rename_files("/path/to/my/documents", ".jpg", "backup_")



# Challenge 9: Create a Python program that creates a user in Linux
# and verifies the creation using the 'subprocess' module.

import subprocess
import sys

# IMPORTANT: Yeh script Linux/macOS par chalega. Windows par 'useradd' command nahi hoti.
# NOTE: User create karne ke liye 'root privileges' (sudo) zaroori hain.

def create_and_verify_user(username):
    """
    Linux mein naya user 'useradd' command se banata hai aur phir 'id' command se verify karta hai.
    """
    print(f"\n--- Starting process for user: {username} ---")

    # 1. User Creation Command (Humein root privileges (sudo) chahiye)
    # '-m' flag user ke liye home directory bhi bana deta hai
    create_cmd = ["sudo", "useradd", "-m", username]
    
    print(f"Attempting to run: {' '.join(create_cmd)}")

    try:
        # User banane ki koshish karo
        creation_result = subprocess.run(
            create_cmd,
            capture_output=True,
            text=True,
            check=False # Check=False rakhenge taki hum status code khud handle karein
        )
        
        # 2. Check Creation Status
        if creation_result.returncode == 0:
            print(f"Status: SUCCESS! User '{username}' created successfully.")
        elif creation_result.returncode == 9:
             # useradd ka return code 9 ka matlab hai user already exist karta hai
            print(f"Status: WARNING! User '{username}' already exists (Code 9).")
        else:
            print(f"Status: FAILED! User creation failed (Code {creation_result.returncode}).")
            print(f"Error Output:\n{creation_result.stderr.strip()}")
            return # Agar creation fail hua, toh aage verify nahi karenge
            
    except FileNotFoundError:
        print("ERROR: 'useradd' command nahi mili. Check karo ki tum Linux/macOS use kar rahe ho.")
        return
    except Exception as e:
        print(f"An unexpected error occurred during user creation: {e}")
        return

    # 3. User Verification Command (id command se check karo)
    verify_cmd = ["id", username]
    print(f"\nAttempting to run verification: {' '.join(verify_cmd)}")
    
    try:
        verification_result = subprocess.run(
            verify_cmd,
            capture_output=True,
            text=True,
            check=True # Agar verification fail hua, toh exception throw hoga
        )
        
        # Agar return code 0 hai aur id output mila, toh verification success
        if verification_result.returncode == 0:
            print("Verification: SUCCESS! User details found.")
            print(f"User Details:\n{verification_result.stdout.strip()}")
        
    except subprocess.CalledProcessError:
        print(f"Verification: FAILED! User '{username}' details nahi mile. Creation fail ho gaya tha.")
    except Exception as e:
        print(f"An unexpected error occurred during verification: {e}")


if __name__ == "__main__":
    # Naya user name jo tum banana chahte ho
    new_user = "devops_intern"
    
    print("--- Linux User Management Script ---")
    print(f"NOTE: To run this, you MUST use 'sudo python {sys.argv[0]}' in terminal.")
    
    # 1. User create aur verify karo
    create_and_verify_user(new_user)

    # 2. Ek baar phir se chalao to check the 'already exists' warning
    # create_and_verify_user(new_user)
