# 🐍 Day 8: File Handling, Exception Handling & Modules

## 📘 Overview
This lesson covers how Python handles files, manages runtime errors using exceptions, and utilizes built-in modules.  
You’ll learn how to **read**, **write**, **append**, and **delete** files — along with handling errors safely and exploring some common Python libraries like `math`, `random`, and `time`.

---

## 📂 Topics Covered
- File Handling  
- File Modes (`r`, `w`, `a`, `x`, `t`, `b`, `+`)  
- Reading and Writing Files  
- Exception Handling (`try`, `except`, `else`, `finally`, `raise`)  
- Custom Exceptions  
- Python Modules (`math`, `random`, `time`, `os`)  

---

## 📁 File Modes Summary

| Mode | Description |
|------|--------------|
| `'r'` | Read file (must exist). |
| `'w'` | Write and overwrite existing file. |
| `'x'` | Create new file (error if exists). |
| `'a'` | Append data to existing file. |
| `'b'` | Binary mode. |
| `'t'` | Text mode (default). |
| `'+'` | Read and write mode combined. |

---

## 🧾 File Handling Examples

### ✅ Reading a File
```python
f = open("sample.txt", "r")
print(f.read())
f.close()

