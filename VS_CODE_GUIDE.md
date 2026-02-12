# 🚀 VS CODE SE RUN KAISE KARE

## 📋 Quick Setup (3 Steps Only!)

### STEP 1: Files Setup
```
1. Desktop par folder banao: CV_Project
2. In 2 files ko us folder mein rakho:
   - app.py
   - requirements.txt
```

### STEP 2: VS Code Mein Open Karo
```
1. VS Code kholo
2. File → Open Folder
3. CV_Project folder select karo
```

### STEP 3: Run Karo
```
1. app.py file kholo VS Code mein
2. Terminal kholo (Ctrl + `)
3. Type karo:
   pip install gradio opencv-python numpy pillow
4. Phir type karo:
   python app.py
5. Browser automatically khulega! 🎉
```

---

## 📺 VS CODE DETAILED GUIDE

### Opening Terminal in VS Code:
```
Method 1: Ctrl + ` (backtick key)
Method 2: View → Terminal
Method 3: Terminal → New Terminal
```

### First Time Setup:
```bash
# Terminal mein ek-ek line run karo:

# 1. Check Python
python --version

# 2. Install packages
pip install gradio opencv-python numpy pillow

# 3. Run app
python app.py
```

### Har Baar Run Karne Ke Liye:
```bash
# Bas ye ek command:
python app.py
```

---

## 🎯 VS CODE SHORTCUTS

### Useful Shortcuts:
```
Ctrl + `       → Terminal toggle
Ctrl + S       → Save file
Ctrl + P       → Quick file open
F5             → Run with debugger
Ctrl + C       → Stop app (terminal mein)
```

### Running Options:

**Option 1 - Terminal:**
```bash
python app.py
```

**Option 2 - Run Button:**
```
Right-click on app.py → Run Python File in Terminal
```

**Option 3 - Debug:**
```
F5 press karo → Python File select karo
```

---

## 📁 Folder Structure

```
CV_Project/
├── app.py                    ← Main file (minimal code!)
├── requirements.txt          ← Dependencies
└── README.md                 ← This guide
```

**That's it! Clean & simple!**

---

## 💡 Pro Tips for VS Code

### Install Useful Extensions:
```
1. Python (Microsoft)
2. Pylance
3. Python Indent
```

### Auto-format Code:
```
Shift + Alt + F  → Format code beautifully!
```

### Quick Run Setup:
```
1. Create file: .vscode/launch.json
2. Add this:
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Run CV App",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/app.py",
            "console": "integratedTerminal"
        }
    ]
}
3. Now press F5 to run directly!
```

---

## 🐛 Common Issues in VS Code

### "Python not found"
**Solution:**
```
1. Install Python from python.org
2. Restart VS Code
3. Select Python interpreter: Ctrl+Shift+P → "Python: Select Interpreter"
```

### "pip not recognized"
**Solution:**
```bash
python -m pip install gradio opencv-python numpy pillow
```

### Terminal not showing
**Solution:**
```
View → Terminal (or Ctrl + `)
```

### Port already in use
**Solution:**
```python
# In app.py, last line change to:
demo.launch(server_port=7861)
```

---

## ✅ CHECKLIST

- [ ] VS Code installed
- [ ] Python installed
- [ ] Folder created (CV_Project)
- [ ] Files copied (app.py, requirements.txt)
- [ ] Folder opened in VS Code
- [ ] Terminal opened (Ctrl + `)
- [ ] Packages installed (pip install...)
- [ ] App running (python app.py)
- [ ] Browser mein app dikha

---

## 🎓 Why This Code is Better

### Original vs New:
```
Original: 600+ lines
New:      150 lines  ← 75% smaller! 🎯

Original: Multiple files
New:      Single file ← Simple!

Original: Complex structure
New:      Clean classes ← Professional!
```

### Code Quality:
```
✓ Minimal imports
✓ Clean functions
✓ No repetition
✓ Good practices
✓ Professional structure
✓ Easy to understand
```

---

## 🚀 FINAL STEPS

```bash
# Open VS Code
# Open Terminal (Ctrl + `)
# Run these:

pip install gradio opencv-python numpy pillow
python app.py

# Browser khulega → Enjoy! 🎉
```

**Simple hai! Just 2 commands! 💪**
