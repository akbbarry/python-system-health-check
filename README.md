
# Python System Health Check

A beginner DevOps project built with Python on Debian Linux using a Chromebook Linux development environment.

## Overview

This script checks basic system information and disk usage. It reports whether available disk space is above a defined threshold.

## Features

- Displays the current date and time
- Identifies the operating system
- Displays the Python version
- Reports total and available disk space
- Calculates disk usage percentage
- Warns when free disk space falls below 2 GB

## Technologies

- Python 3
- Linux (Debian 13)
- Git and GitHub
- Python virtual environments

## How to Run

Clone the repository:

```bash
git clone https://github.com/akbbarry/python-system-health-check.git
cd python-system-health-check
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Run the script:

```bash
python3 system_check.py
```

## What I Learned

- Using Linux commands
- Writing Python automation scripts
- Checking disk usage programmatically
- Managing code with Git
- Publishing a project on GitHub

## Future Improvements

- Add CPU and memory monitoring
- Write results to a log file
- Add automated tests
- Create a CI pipeline with GitHub Actions

---

Created as part of my hands-on DevOps practice.
