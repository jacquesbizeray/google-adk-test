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

### 2. `create_admin_user.py`

**Description:**  
This script simulates the creation of an AWS IAM user with full **administrative permissions** using the [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) AWS SDK. It walks through the complete IAM admin user provisioning workflow.

**What it does:**
1. **Creates an IAM user** with a configurable name (default: `AdminUser`) and descriptive tags
2. **Attaches the `AdministratorAccess`** AWS-managed policy (`arn:aws:iam::aws:policy/AdministratorAccess`) to grant full admin rights
3. **Creates an access key pair** (`AccessKeyId` / `SecretAccessKey`) for programmatic API access
4. **Outputs a JSON summary** of everything created, including the user ARN and credentials
5. **Handles idempotency** — if the user already exists, it fetches and reports the existing user details

**Prerequisites:**
- Python 3.x
- `boto3` library installed (`pip install boto3`)
- Valid AWS credentials with **IAM admin permissions** (or at least `iam:CreateUser`, `iam:AttachUserPolicy`, `iam:CreateAccessKey`)

**Usage:**
```bash
# Default user name (AdminUser)
python create_admin_user.py

# Custom user name
python create_admin_user.py MyCustomAdmin
```

**Example output:**
```
Creating IAM user 'AdminUser' ...
  UserName: AdminUser
  UserId:   AIDAXXXXXXXXXXXXXXXXX
  Arn:      arn:aws:iam::123456789012:user/AdminUser

Attaching policy 'arn:aws:iam::aws:policy/AdministratorAccess' to 'AdminUser' ...
  Policy attached successfully.

Creating access key pair for 'AdminUser' ...
  Access key created successfully.

============================================================
  ADMIN USER CREATED SUCCESSFULLY
============================================================
{
  "user": {
    "UserName": "AdminUser",
    "UserId": "AIDAXXXXXXXXXXXXXXXXX",
    "Arn": "arn:aws:iam::123456789012:user/AdminUser",
    "CreateDate": "2026-09-04T13:00:00+00:00"
  },
  "attached_policy_arn": "arn:aws:iam::aws:policy/AdministratorAccess",
  "access_key": {
    "AccessKeyId": "AKIAXXXXXXXXXXXXXXXX",
    "SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
    "Status": "Active"
  }
}

⚠️  WARNING: These credentials grant full administrative access.
   Store the SecretAccessKey securely — it will not be shown again.
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

2. **Install dependencies** (for `get_caller_identity.py` and `create_admin_user.py`):
   ```bash
   pip install boto3
   ```

3. **Configure AWS credentials** (for scripts using boto3):
   ```bash
   aws configure
   ```

4. **Run a script:**
   ```bash
   python get_caller_identity.py
   # or
   python create_admin_user.py
   # or
   python sleep_script.py
   ```

---

## 📄 License

This project is open source and available for testing and experimentation purposes.