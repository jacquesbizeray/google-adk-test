import boto3


def main():
    """Create a boto3 sts client and call get_caller_identity."""
    try:
        sts_client = boto3.client("sts")
        response = sts_client.get_caller_identity()
        print("Successfully retrieved AWS caller identity:")
        print(f"  UserId:    {response.get('UserId')}")
        print(f"  Account:   {response.get('Account')}")
        print(f"  Arn:       {response.get('Arn')}")
    except Exception as e:
        print(f"Error calling AWS STS get_caller_identity: {e}")


if __name__ == "__main__":
    main()
