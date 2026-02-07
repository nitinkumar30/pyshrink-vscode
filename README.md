# PyShrink – Clean & Shrink Python Projects in VS Code

🚀 **PyShrink** is a Visual Studio Code extension that helps you **clean, shrink, and prepare Python projects for sharing** directly from your workspace.

It runs a Python-based cleanup CLI (`pyshrink_cli.py`) to remove unnecessary files and folders from a **cloned copy** of your project—keeping the original code completely safe.  
PyShrink is ideal for **enterprise, internal, and restricted Git environments** where teams frequently share code as ZIPs instead of repositories.

---

## Working

<img
  src="screenrecordings/pyshrink_vscodeExtension_GIF.gif"
  alt="PyShrink VS Code extension"
/>

---

## Why PyShrink?

- Reduce project size before sharing
- Avoid manual cleanup and repeated zipping
- Keep original projects untouched
- Works without Git or external services
- Designed for corporate and internal workflows

---

## Features

- 🧹 Clean Python projects directly from VS Code
- 🧪 Interactive cleanup mode
- ⚙️ Run cleanup with custom CLI arguments
- 📁 Automatically detects the active workspace folder
- 🔒 Works on a cloned copy (original project is never modified)
- 🖥️ Real-time output via VS Code notifications

---

## Screenshots & Demo

> _Screenshots and animations help users understand the workflow quickly._

### Command Palette Integration
![Command Palette](images/command-palette.png)

### Interactive Cleanup
![Interactive Cleanup](images/interactive-clean.gif)

### Run with Arguments
![Arguments Mode](images/arguments-mode.png)

_(Add your screenshots/GIFs under an `images/` folder)_

---

## Commands (Aligned with `package.json`)

The following commands are contributed by this extension:

### **PyShrink: Clean Project**
**Command ID:** `pyshrink.clean`

Runs PyShrink in interactive mode using default behavior.

---

### **PyShrink: Run with Arguments**
**Command ID:** `pyshrink.args`

Prompts the user to enter CLI arguments and passes them directly to the PyShrink CLI.

**Example input:**
```

--req --readme

````

Executed as:
```bash
python main.py --req --readme
````

---

### **PyShrink: Hello**

**Command ID:** `pyshrink.hello`

Simple test command to verify that the extension is activated.

---

## Quick Setup (1 Minute)

1. **Install Python 3**

   * Ensure Python 3.x is installed and accessible via `python`

2. **Open your project folder in VS Code**

   * Use **File → Open Folder**
   * Do not open individual files

3. **Ensure PyShrink CLI exists**

   * `pyshrink_cli.py` must be present in the workspace root

4. **Run PyShrink**

   * Press `Ctrl + Shift + P`
   * Select **PyShrink: Clean Project**
     or **PyShrink: Run with Arguments**

---

## Requirements

To use **PyShrink**, the following prerequisites must be met:

* **Python 3.x installed on the system**

  ```bash
  python --version
  ```

* **`python` available in system PATH**

  * The extension spawns Python using the `python` command

* **A workspace folder opened in VS Code**

  * The extension does not work with single files

* **`pyshrink_cli.py` present in the workspace root**

  * This is the entry point for the cleanup logic

> ⚠️ The extension does not install Python dependencies automatically.

---

## OS-Specific Notes

### 🪟 Windows

* Install Python with **“Add Python to PATH”** enabled
* Restart VS Code after installation
* Verify:

  ```cmd
  where python
  ```

---

### 🍎 macOS

* Install Python via official installer or Homebrew
* Ensure `python` points to Python 3:

  ```bash
  python --version
  ```

---

### 🐧 Linux

* Install Python via package manager:

  ```bash
  sudo apt install python3
  ```
* Ensure `python` resolves correctly

---

## Expected Project Structure

```text
your-project/
├── pyshrink_cli.py
├── config.py
├── src/
├── tests/
├── requirements.txt
└── README.md
```

---

## Extension Settings

This extension does **not** add VS Code settings via `contributes.configuration`.

All behavior is controlled through:

* CLI arguments
* `config.py` inside the project

---

## Common Setup Mistakes

### ❌ No workspace folder found

* Open the project folder, not a file

### ❌ Python not found

* Python not in PATH
* Restart VS Code after installing Python

### ❌ `pyshrink_cli.py` missing

* Ensure the file exists at the workspace root

### ❌ No visible output

* Check **Help → Toggle Developer Tools** for logs

---

## Known Issues

* Assumes `python` command (not `python3`)
* Long output may be truncated in notifications
* No progress bar UI
* CLI arguments are not validated

---

## Release Notes

### 1.0.0

* Initial release
* Interactive cleanup command
* Argument-based execution
* Python subprocess integration
* Workspace auto-detection

---

## Keywords (Marketplace SEO)

**python, cleanup, project-cleaner, shrink, zip, enterprise, internal-tools, automation, vscode-extension, python-tools**

---

**Enjoy using PyShrink 🚀**

```
