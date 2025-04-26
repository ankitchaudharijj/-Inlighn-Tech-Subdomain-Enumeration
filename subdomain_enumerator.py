# subdomain_enumerator.py

import threading
import requests

# Target domain
domain = 'youtube.com'

# List to store discovered subdomains
discovered_subdomains = []

# Lock for thread-safe operations
lock = threading.Lock()

# Function to check if a subdomain exists
def check_subdomain(subdomain):
    url = f"http://{subdomain}.{domain}"
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            print(f"[+] Discovered subdomain: {url}")
            with lock:
                discovered_subdomains.append(url)
    except requests.ConnectionError:
        pass  # If connection fails, subdomain does not exist
    except requests.Timeout:
        pass  # If it times out, also treat it as non-existent

# Read subdomains from file
with open('subdomains.txt', 'r') as file:
    subdomains = file.read().splitlines()

# List to keep track of threads
threads = []

# Create and start a thread for each subdomain
for subdomain in subdomains:
    t = threading.Thread(target=check_subdomain, args=(subdomain,))
    t.start()
    threads.append(t)

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Write discovered subdomains to a file
with open('discovered_subdomains.txt', 'w') as file:
    for subdomain in discovered_subdomains:
        file.write(subdomain + '\n')

print("\nEnumeration complete. Discovered subdomains saved to discovered_subdomains.txt.")
