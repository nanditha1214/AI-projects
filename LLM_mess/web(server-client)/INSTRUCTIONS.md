# Installing and Running DeepSeek-R1 on Ollama

## System Requirements

### My Specs:
- **GPU**: No external GPU (Integrated Graphics Only)
- **CPU**: Intel i5 6th Gen
- **RAM**: 16 GB (Recommended for DeepSeek)
- **Storage**: 512 GB SSD
- **OS**: Windows 10 (Windows 11 should work fine)

### Minimum Recommended Specs:
- **GPU**: No external GPU
- **CPU**: Any CPU released after 2018
- **RAM**: 8 GB (16 GB recommended for larger models)
- **Storage**: 512 GB SSD
- **OS**: Any Modern OS(newer than Big Sur for Mac, Windows 10/11 for Windows), Provided that you are familiar with it
### Ideal Specs:
- **GPU**: No external GPU
- **CPU**: Any CPU released after 2018
- **RAM**: 32 GB
- **Storage**: 1 TB SSD
- **OS**: Any (Linux requires manual command-line installation for Ollama, which is not covered here)

---

## Installation Steps

### **1) Ensure Python is Installed**
- Python **3.9+** is recommended.
- Run `python --version` in the command prompt to check your version.
- Some modules may not support **older versions** (earlier than Python 3.10).
- Pre-release versions might have issues
- Visit [Python Downloads](https://www.python.org/downloads/) do download python

### **2) Download Ollama**
- Visit [https://ollama.com/download](https://ollama.com/download) and download the installer for your OS.
- The download may take **up to 10 minutes**.
- **Linux Note:** If you're using Linux, you may encounter installation issues. The setup process may require additional manual steps.

![Download Ollama](https://github.com/user-attachments/assets/b9547ad9-12df-4e38-acdd-49e561ad02aa)

### **3) Install Ollama**
- Run the downloaded file and follow the **on-screen instructions**.
- After installation, the installer will **close abruptly**. This is normal—wait **30 seconds** for the service to stabilize.
- On Windows, check the **system tray** for the Ollama icon.

![Ollama System Tray](https://github.com/user-attachments/assets/677e12b8-c110-453d-ad5e-0ea835b12591)

- Open [http://localhost:11434/](http://localhost:11434/) in your browser to confirm Ollama is running.
  - If you see "Ollama is running," the installation is successful.
  - If not, open the Ollama app and retry.

### **4) Open Command Prompt**
- Open the Windows **Command Prompt (cmd)** and keep it open for the next steps.

![Command Prompt](https://github.com/user-attachments/assets/2c319c83-2073-4ff7-875f-18988095c5de)

### **5) Download DeepSeek-R1 Model**
- Visit [https://ollama.com/library/deepseek-r1](https://ollama.com/library/deepseek-r1).
- Follow the instructions to copy the model download command.
- Paste the command into the command prompt and press **Enter**.
- The model **download may take up to an hour**.
  - If it fails, re-run the command. It will begin from where it left
  - It may take **several attempts (up to 9 times)** to complete.
  - If it seems like the bar is moving backwards, just ignore. It may be pulling other needed filed
  - **  Pressing `CTRL + C` will cancel the install, even if you meant to copy something **

![DeepSeek Model Install](https://github.com/user-attachments/assets/1d2bb51d-104e-4de7-b88c-813a5434a2cb)

### **6) Run DeepSeek-R1**
- After downloading, start the model using:
  ```sh
  ollama run deepseek-r1:1.5b
  ```
- The model may take time to process requests and may produce **unexpected responses**.
- Each response consists of two phases:
  - **Thinking phase** (processing input)
  - **Reply phase** (generating output)

![DeepSeek Output](https://github.com/user-attachments/assets/168430f6-8d5d-41a6-9d5e-e1f097802bd3)

### **7) Install Python Ollama Package**
- Run the following command to interact with Ollama using Python:
  ```sh
  pip install ollama
  ```

### **8) Running Other Models**
- To install and run the **LLaMA** model, use:
  ```sh
  ollama run llama
  ```
- Some scripts may reference **LLaMA** instead of **DeepSeek**. Consider checking model names in your scripts to ensure compatibility.

---

## Conclusion
This guide walks you through installing Ollama, downloading the DeepSeek-R1 model, and setting up a Python environment for interacting with it. Once installed, you can start using **DeepSeek-R1** or explore other models from the **Ollama library**.

