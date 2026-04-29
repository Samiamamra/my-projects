# How to Run Downloaded Python Projects (Beginner Guide)

This guide explains how to run Python programs after downloading them from a repository (like GitHub), even if you have no programming experience.
## 1. Download the project:

Open the GitHub repository page in your browser(you will find the links in the web site)

Click the green button Code

Select Download ZIP

Wait for download to finish

Right-click the ZIP file and choose Extract All (or unzip it)

Open the extracted folder

You now have the full project on your computer.
---

## 2. What You Need First

Before running any Python project, make sure you have:

###  Python Installed

* Download from: [https://www.python.org/downloads/](https://www.python.org/downloads/)
* IMPORTANT: During installation, check **"Add Python to PATH"**

### A Folder with the Project

After downloading a project (usually as a ZIP file), you should:

* Extract (unzip) the file
* Open the extracted folder

---

## 3. Open the Project Folder in Terminal

### On Windows:

1. Open the project folder
2. Click on the address bar at the top
3. Type:

```
cmd
```

4. Press Enter

This opens Command Prompt inside the project folder.

---

## 4. Run the Python Program

Look for the file that ends with ".py"
ex "main.py"

Then run it using:

```
python main.py
```

(Replace `main.py` with the correct file name if different)

---

## 5. Common Issues

###  "Python is not recognized"

 Fix: Reinstall Python and enable "Add to PATH"

---

###  Module not found error

 Fix: Install missing packages using pip:

```
pip install module_name
```

---

###  Nothing happens or program closes

Fix: Run it from terminal (not by double-clicking)

---

## 6. Important Notes

* Always run the program from inside its folder
* Do NOT move files around unless you know what you're doing
* Read README.md file if it exists (it usually explains how to run the project)

---

## 7. Final Advice

Running downloaded Python projects is mostly about:

* Opening the folder correctly
* Installing dependencies
* Running the main file

