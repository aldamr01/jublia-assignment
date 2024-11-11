# Jublia Assignment

Jublia assignment project.

## Table of Contents
- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Testing](#testing)
- [License](#license)

## About
Simple email broadcaster WebApp.

## Features
- Email blaster with schedule

## Installation

### Prerequisites
- [Python 3.x](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)
- [RabbitMQ]()
- [MySQL8]()

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/aldamr01/jublia-assignment
   cd jublia-assignment

2. **Install dependencies**
    ```bash
    pip install -r requirements.txt

3. **Modify the env**
    - fill the `MYSQL_*` environment variable using your MySQL credentials.
    - etc.

4. **Initialize database**
    - create a new DB in your machine.
    - then run this command:
    ```bash
    flask init-db

5. **Run development app**
    ```bash
    python app.py
