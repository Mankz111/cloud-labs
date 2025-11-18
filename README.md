# ✨ Cloud, DevOps, & Automation Lab

Repository for studies, labs, and small projects related to Cloud Computing, DevOps, and automation. This is where I store scripts, experiments, and practical examples that I create while learning and working in the cloud ecosystem.

---

## 🏗️ Repository Structure

| Directory | Content | Focus |
| :--- | :--- | :--- |
| **`Scripts/`** | Useful scripts or automation tools (Python, Bash, etc.) | Automation |
| **`docker/`** | Experiments with Docker, Dockerfiles, and docker-compose | Containerization |
| **`terraform/`** | Infrastructure-as-Code (IaC) examples using Terraform | IaC |
| **`README.md`** | Documentation | Doc |

---

## 🇵🇹 Featured Project: Portuguese NIF Validation

### 📂 `Scripts/validate_nif.py`

**Context:**
This Python script was developed as part of a university course project focused on file automation for accounting workflows.

### 🐛 The Problem: OCR Inaccuracy
During the project, we used Power Automate to extract information from scanned documents using OCR. However, the Windows OCR engine often misinterpreted the digit **"0" (zero)**—especially when printed with a diagonal slash—as the number **"8"**.

Because NIF (*Portuguese tax identification number*) validation is mathematically sensitive, these OCR mistakes caused critical errors in the data pipeline.

### 💡 The Solution
To solve this, I created a Python script that robustly handles these errors. It:

* ✅ **Validates** whether a given NIF is mathematically correct.
* 🔍 **Detects** specific OCR misinterpretations (specifically the "0" vs "8" issue).
* 🔄 **Replaces** incorrect characters intelligently when a potential match is found.
* 🔒 **Ensures** that the final output is a valid, usable NIF.
