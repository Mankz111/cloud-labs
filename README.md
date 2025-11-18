# cloud-labs

Repository for studies, labs, and small projects related to Cloud Computing, DevOps, and automation.
This is where I store scripts, experiments, and practical examples that I create while learning and working in the cloud ecosystem.

Repository Structure
cloud-lab/
 ├── Scripts/        # Useful scripts or automation tools (Python, Bash, etc.)
 ├── docker/         # Experiments with Docker, Dockerfiles, and docker-compose
 ├── terraform/      # Infrastructure-as-Code (IaC) examples using Terraform
 └── README.md

Current Content
Scripts/
 ├── validate_nif.py — Python script to validate Portuguese NIF numbers.
     This script was developed as part of a university course project focused on file automation for accounting workflows.
     
    During the project, we used Power Automate to extract information from scanned documents using OCR. However, the Windows OCR engine frequently misread certain digits:
    The digit "0" (zero), especially when printed with a diagonal slash, was often interpreted as "8".
    Because NIF (Portuguese tax identification number) validation is sensitive to digit accuracy, these OCR mistakes caused incorrect results.
    
    To solve this, I created a Python script that:
    
    Checks whether a given NIF is valid
    Detects OCR misinterpretations related to "0" and "8"
    Replaces incorrect characters when needed
    
    Ensures that the final output is a correctly validated NIF
