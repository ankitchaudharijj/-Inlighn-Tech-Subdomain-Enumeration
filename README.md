
# Subdomain Enumeration Tool

A Python-based tool to discover active subdomains of a target domain using multithreading and HTTP requests.

---

## 📋 Project Description

This tool helps in identifying active subdomains of a given domain (like `youtube.com`) by sending HTTP requests to potential subdomains.  
It is useful for **reconnaissance** during cybersecurity assessments and penetration testing.

The tool is optimized using **multithreading**, making the enumeration process much faster compared to sequential testing.

---

## 🚀 Features

- Fast subdomain scanning using multithreading
- Saves discovered subdomains into a file
- Error handling for connection issues
- Simple and easy to use
- Beginner-friendly codebase

---

## 🛠️ Prerequisites

- **Python 3.x** installed
- Install required library:
  ```bash
  pip install requests
  ```

---

## 📂 Project Structure

```
Subdomain_Enumerator_Project/
|
├── subdomain_enumerator.py      # Main Python script
├── subdomains.txt               # List of potential subdomains (input file)
└── discovered_subdomains.txt    # Found subdomains (output file)
```

---

## 📜 Usage Instructions

1. **Clone the repository** or download the files.
2. **Prepare the `subdomains.txt`** file with a list of subdomains to test.
   Example:
   ```
   www
   mail
   blog
   admin
   api
   ```
3. **Run the script**:
   ```bash
   python subdomain_enumerator.py
   ```
4. **Result**:
   - Discovered subdomains will be printed in the terminal.
   - All found subdomains will be saved in `discovered_subdomains.txt`.

---

## 📈 How It Works

- Reads subdomains from `subdomains.txt`.
- Forms URLs like `http://subdomain.domain.com`.
- Sends HTTP GET requests to check if the subdomain is alive.
- Uses multiple threads for faster enumeration.
- Saves all active subdomains in an output file.

---

## ✨ Example Output

```
[+] Discovered subdomain: http://www.youtube.com
[+] Discovered subdomain: http://mail.youtube.com
[+] Discovered subdomain: http://api.youtube.com

Enumeration complete. Discovered subdomains saved to discovered_subdomains.txt.
```

---

## 👨‍💻 Author

**Ankit Chaudhari**  
Cybersecurity Enthusiast | Ethical Hacker | Network Auditor

- **University:** Delhi Skill and Entrepreneurship University
- **Certification:** Certified Ethical Hacker (CEH v12)
- **Skills:** Cybersecurity, Ethical Hacking, Network Auditing, VAPT
- **GitHub:** [@ankitchaudharijj](https://github.com/ankitchaudharijj)
- **LinkedIn:** [Ankit Chaudhari](https://www.linkedin.com/in/ankit-chaudhari-40346b318/)

---

## 📄 License

This project is intended for **educational purposes** and **ethical use only**.  
Unauthorized malicious use is strictly prohibited.

---

# 🛡️ Happy Hacking! 🚀
