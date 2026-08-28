# google-adk-test

A collection of Python utility scripts for testing AWS and general utility purposes.

---

## 📁 Scripts

### 1. `get_caller_identity.py`

**Description:**  
This script uses the [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) AWS SDK to call the AWS STS (Security Token Service) `get_caller_identity` API. It retrieves and displays information about the IAM identity currently being used to make API calls.

**What it does:**
- Creates a `boto3` STS client
- Calls `get_caller_identity()` to fetch the current AWS identity
- Prints the following information:
  - **UserId**: The unique identifier of the calling entity
  - **Account**: The AWS account ID
  - **Arn**: The Amazon Resource Name (ARN) of the calling entity

**Prerequisites:**
- Python 3.x
- `boto3` library installed (`pip install boto3`)
- Valid AWS credentials configured (via environment variables, `~/.aws/credentials`, or an IAM role)

**Usage:**
```bash
python get_caller_identity.py
```

**Example output:**
```
Successfully retrieved AWS caller identity:
  UserId:    AIDAXXXXXXXXXXXXXXXXX
  Account:   123456789012
  Arn:       arn:aws:iam::123456789012:user/my-user
```

---

### 2. `sleep.py`

**Description:**  
A simple utility script that pauses execution for 30 seconds. Useful for testing delays, simulating wait times, or as a placeholder in pipelines.

**What it does:**
- Prints a message indicating the sleep has started
- Waits for **30 seconds**
- Prints a completion message

**Prerequisites:**
- Python 3.x (no external dependencies)

**Usage:**
```bash
python sleep.py
```

**Example output:**
```
Sleeping for 30 seconds...
Done!
```

---

### 3. `sleep_script.py`

**Description:**  
A utility script that pauses execution for 45 seconds. Useful for testing delays, simulating longer wait times, or as a placeholder in automated workflows and pipelines.

**What it does:**
- Prints a message indicating the sleep has started
- Waits for **45 seconds**
- Prints a completion message

**Prerequisites:**
- Python 3.x (no external dependencies)

**Usage:**
```bash
python sleep_script.py
```

**Example output:**
```
Starting sleep for 45 seconds...
Sleep completed!
```

---

## 🚀 Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/jacquesbizeray/google-adk-test.git
   cd google-adk-test
   ```

2. **Install dependencies** (for `get_caller_identity.py`):
   ```bash
   pip install boto3
   ```

3. **Configure AWS credentials** (for `get_caller_identity.py`):
   ```bash
   aws configure
   ```

4. **Run a script:**
   ```bash
   python get_caller_identity.py
   # or
   python sleep.py
   # or
   python sleep_script.py
   ```

---

## 📄 License

This project is open source and available for testing and experimentation purposes.
