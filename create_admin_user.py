import boto3
import json
import sys


def create_admin_user(username: str = "AdminUser"):
    """
    Simulate creating an AWS IAM user with full administrative permissions.

    This function:
      1. Creates a new IAM user.
      2. Attaches the AWS-managed 'AdministratorAccess' policy.
      3. Creates an access key pair for programmatic access.
      4. Prints the user details and access credentials.

    Args:
        username: The desired IAM user name (default: 'AdminUser').

    Returns:
        A dict containing the created user info, policy ARN, and access keys.
    """
    iam_client = boto3.client("iam")
    admin_policy_arn = "arn:aws:iam::aws:policy/AdministratorAccess"

    # ------------------------------------------------------------------
    # Step 1 — Create the IAM user
    # ------------------------------------------------------------------
    print(f"Creating IAM user '{username}' ...")
    try:
        create_user_response = iam_client.create_user(
            UserName=username,
            Tags=[
                {"Key": "Environment", "Value": "Simulated"},
                {"Key": "CreatedBy", "Value": "google-adk-test"},
            ],
        )
    except iam_client.exceptions.EntityAlreadyExistsException:
        print(f"  -> User '{username}' already exists. Fetching its details.\n")
        create_user_response = iam_client.get_user(UserName=username)
    except Exception as e:
        print(f"  -> Error creating user: {e}")
        sys.exit(1)

    user = create_user_response["User"]
    print(f"  UserName: {user['UserName']}")
    print(f"  UserId:   {user['UserId']}")
    print(f"  Arn:      {user['Arn']}\n")

    # ------------------------------------------------------------------
    # Step 2 — Attach the AdministratorAccess managed policy
    # ------------------------------------------------------------------
    print(f"Attaching policy '{admin_policy_arn}' to '{username}' ...")
    try:
        iam_client.attach_user_policy(UserName=username, PolicyArn=admin_policy_arn)
        print("  Policy attached successfully.\n")
    except Exception as e:
        print(f"  -> Error attaching policy: {e}\n")

    # ------------------------------------------------------------------
    # Step 3 — Create an access key pair
    # ------------------------------------------------------------------
    print(f"Creating access key pair for '{username}' ...")
    try:
        keys_response = iam_client.create_access_key(UserName=username)
        access_key = keys_response["AccessKey"]
        print("  Access key created successfully.\n")
    except Exception as e:
        print(f"  -> Error creating access key: {e}\n")
        access_key = None

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------
    summary = {
        "user": {
            "UserName": user["UserName"],
            "UserId": user["UserId"],
            "Arn": user["Arn"],
            "CreateDate": user["CreateDate"].isoformat(),
        },
        "attached_policy_arn": admin_policy_arn,
        "access_key": {
            "AccessKeyId": access_key["AccessKeyId"],
            "SecretAccessKey": access_key["SecretAccessKey"],
            "Status": access_key["Status"],
        }
        if access_key
        else None,
    }

    print("=" * 60)
    print("  ADMIN USER CREATED SUCCESSFULLY")
    print("=" * 60)
    print(json.dumps(summary, indent=2))

    # ------------------------------------------------------------------
    # Warning about credentials
    # ------------------------------------------------------------------
    if access_key:
        print("\n⚠️  WARNING: These credentials grant full administrative access.")
        print("   Store the SecretAccessKey securely — it will not be shown again.")
        print("   You can use them with the AWS CLI or SDK by running:")
        print(f'   $ export AWS_ACCESS_KEY_ID={access_key["AccessKeyId"]}')
        print(f'   $ export AWS_SECRET_ACCESS_KEY={access_key["SecretAccessKey"]}')

    return summary


if __name__ == "__main__":
    # Allow an optional custom username passed as a command-line argument
    user = sys.argv[1] if len(sys.argv) > 1 else "AdminUser"
    create_admin_user(user)