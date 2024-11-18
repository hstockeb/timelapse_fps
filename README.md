
# Setting Up and Running the Timelapse Script in a Virtual Environment

This guide will walk you through setting up a Python virtual environment, installing the necessary packages, and running the timelapse script.

---

## Prerequisites

1. **Python Installed**: Ensure you have Python 3.6 or higher installed on your system.
   - You can check by running: `python3 --version` or `python --version`.

2. **Pip Installed**: Verify that `pip`, Python's package manager, is installed.
   - Check with: `pip --version`.

---

## Steps to Set Up

### 1. Create a Directory for the Project

```bash
mkdir timelapse_project
cd timelapse_project
```

### 2. Set Up a Virtual Environment

Create a virtual environment inside the project folder.

```bash
python3 -m venv venv
```

This will create a folder named `venv` containing the virtual environment.

### 3. Activate the Virtual Environment

- On **Linux/MacOS**:

    ```bash
    source venv/bin/activate
    ```

- On **Windows**:

    ```cmd
    .\venv\Scripts\activate
    ```

After activation, your terminal prompt should change to indicate the virtual environment is active.

### 4. Install Required Packages

Install the necessary Python packages:

```bash
pip install opencv-python tqdm
```

### 5. Verify Package Installation

To confirm that the packages are installed:

```bash
pip list
```

You should see `opencv-python` and `tqdm` in the list of installed packages.

---

## Running the Script

1. Copy the timelapse script (e.g., `modified_timelapse_subfolders.py`) into the project directory.

2. Run the script:

```bash
python modified_timelapse_subfolders.py
```

Follow the on-screen prompts to configure the video output.

---

## Deactivating the Virtual Environment

When you're done, deactivate the virtual environment:

```bash
deactivate
```

---

## Additional Notes

- If you need to install other packages in the future, ensure the virtual environment is activated before running `pip install`.
- For troubleshooting, check if the virtual environment is active and confirm Python and Pip versions.

---

## License

This project and its documentation are available under the [MIT License](LICENSE).

---
