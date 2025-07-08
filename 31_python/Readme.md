# Python Decorators, File I/O, and Popular Libraries for DevOps

## Table of Contents
- [Python Decorators](#python-decorators)
- [File I/O in Python](#file-io-in-python)
- [Popular Python Libraries for DevOps](#popular-python-libraries-for-devops)

---

## Python Decorators

Decorators are a powerful feature in Python that allow you to modify the behavior of functions or classes. They are often used for logging, access control, timing, and more.

**Example: Logging Decorator**

```python
def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} finished")
        return result
    return wrapper

@log_function
def greet(name):
    print(f"Hello, {name}!")

greet("DevOps Engineer")
```

**Explanation:**  
The `@log_function` decorator wraps the `greet` function, printing messages before and after its execution.

---

## File I/O in Python

Python makes it easy to read from and write to files, which is essential for DevOps tasks like log processing and configuration management.

**Example: Reading and Writing Files**

```python
# Writing to a file
with open('example.txt', 'w') as f:
    f.write('Hello, DevOps!\n')

# Reading from a file
with open('example.txt', 'r') as f:
    content = f.read()
    print(content)
```

**Explanation:**  
- `with open(...)` ensures files are properly closed.
- `'w'` mode writes to the file; `'r'` mode reads from it.

---

## Popular Python Libraries for DevOps

### 1. **os** and **subprocess**
- For interacting with the operating system and running shell commands.

```python
import os
import subprocess

print(os.listdir('.'))  # List files in current directory
subprocess.run(['ls', '-l'])  # Run shell command
```

### 2. **requests**
- For making HTTP requests (e.g., interacting with APIs).

```python
import requests

response = requests.get('https://api.github.com')
print(response.status_code)
```

### 3. **paramiko**
- For SSH connections and remote command execution.

```python
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('hostname', username='user', password='pass')
stdin, stdout, stderr = ssh.exec_command('ls')
print(stdout.read().decode())
ssh.close()
```

### 4. **PyYAML**
- For parsing YAML configuration files.

```python
import yaml

with open('config.yaml') as f:
    config = yaml.safe_load(f)
print(config)
```

---

## Summary

- **Decorators** help modify function behavior.
- **File I/O** is essential for automation and scripting.
- **Popular libraries** like `os`, `subprocess`, `requests`, `paramiko`, and `PyYAML` are invaluable for DevOps tasks.
