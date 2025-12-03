# 🐳 Go Web Server & Networking Lab

This directory contains a containerized Go application and experiments with Docker networking and Load Balancing using Caddy.

## 📂 Project Overview

* **Language:** Go (Golang) 1.23+
* **Base Image:** `debian:stable-slim`
* **Key Concepts:** Cross-compilation, Docker Networking, Reverse Proxy.

---

## 🛠️ Go Server: Building from Windows

This project was developed on a **Windows** host but runs inside a **Linux** container. To avoid the `exec format error`, the binary must be cross-compiled targeting Linux before building the Docker image.

### 1. Compile for Linux (PowerShell)
Run these commands in the project root to generate the correct binary:

```powershell
# Set environment variables for Linux compilation
$Env:GOOS = "linux"
$Env:GOARCH = "amd64"

# Build the binary (output name must match Dockerfile COPY instruction)
go build -o cloud-labs .
