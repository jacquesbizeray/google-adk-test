import boto3
import json
import sys


def open_security_group(group_name: str = "OpenToWorldSG", description: str = "⚠️  WARNING: Security group open to the world"):
    """
    Simulate creating an EC2 security group with inbound rules open to 0.0.0.0/0.

    This function:
      1. Creates a new EC2 security group in the default VPC.
      2. Adds inbound rules allowing all TCP traffic from 0.0.0.0/0.
      3. Adds inbound rules allowing all UDP traffic from 0.0.0.0/0.
      4. Adds inbound rules allowing ICMP (ping) from 0.0.0.0/0.
      5. Prints the security group details.

    Args:
        group_name: The name of the security group (default: 'OpenToWorldSG').
        description: A description for the group (default includes a warning).

    Returns:
        A dict containing the security group ID and a summary of the rules.
    """
    ec2_client = boto3.client("ec2")

    # ------------------------------------------------------------------
    # Step 1 — Create the security group
    # ------------------------------------------------------------------
    print(f"Creating security group '{group_name}' ...")
    try:
        create_response = ec2_client.create_security_group(
            GroupName=group_name,
            Description=description,
            TagSpecifications=[
                {
                    "ResourceType": "security-group",
                    "Tags": [
                        {"Key": "Environment", "Value": "Simulated"},
                        {"Key": "CreatedBy", "Value": "google-adk-test"},
                    ],
                },
            ],
        )
        group_id = create_response["GroupId"]
        print(f"  GroupId:   {group_id}")
        print(f"  GroupName: {group_name}")
        print(f"  VPC:       Default VPC\n")
    except ec2_client.exceptions.SecurityGroupAlreadyExistsException:
        print(f"  -> Security group '{group_name}' already exists. Fetching its details.\n")
        describe_response = ec2_client.describe_security_groups(
            Filters=[{"Name": "group-name", "Values": [group_name]}],
        )
        sg = describe_response["SecurityGroups"][0]
        group_id = sg["GroupId"]
        print(f"  GroupId:   {group_id}")
        print(f"  GroupName: {sg['GroupName']}")
        print(f"  VpcId:     {sg.get('VpcId', 'N/A')}\n")
        # Return early with existing details
        return {
            "group_id": group_id,
            "group_name": group_name,
            "description": sg.get("Description", ""),
            "vpc_id": sg.get("VpcId", "N/A"),
            "note": "Security group already existed — no rules were modified.",
        }
    except Exception as e:
        print(f"  -> Error creating security group: {e}")
        sys.exit(1)

    # ------------------------------------------------------------------
    # Step 2 — Add inbound rules open to the world (0.0.0.0/0)
    # ------------------------------------------------------------------
    print("Adding inbound rules open to 0.0.0.0/0 ...")

    inbound_permissions = [
        {
            "IpProtocol": "tcp",
            "FromPort": 0,
            "ToPort": 65535,
            "IpRanges": [{"CidrIp": "0.0.0.0/0", "Description": "All TCP traffic from anywhere"}],
        },
        {
            "IpProtocol": "udp",
            "FromPort": 0,
            "ToPort": 65535,
            "IpRanges": [{"CidrIp": "0.0.0.0/0", "Description": "All UDP traffic from anywhere"}],
        },
        {
            "IpProtocol": "icmp",
            "FromPort": -1,
            "ToPort": -1,
            "IpRanges": [{"CidrIp": "0.0.0.0/0", "Description": "ICMP (ping) from anywhere"}],
        },
    ]

    try:
        ec2_client.authorize_security_group_ingress(
            GroupId=group_id,
            IpPermissions=inbound_permissions,
        )
        print("  ✅  Inbound rules added successfully.\n")
    except Exception as e:
        print(f"  -> Error adding inbound rules: {e}\n")

    # ------------------------------------------------------------------
    # Step 3 — Optionally allow all outbound (already default, but print it)
    # ------------------------------------------------------------------
    print("Outbound rules: All traffic allowed by default (0.0.0.0/0).\n")

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------
    summary = {
        "group_id": group_id,
        "group_name": group_name,
        "description": description,
        "inbound_rules": [
            {
                "protocol": "ALL TCP",
                "ports": "0-65535",
                "source": "0.0.0.0/0",
            },
            {
                "protocol": "ALL UDP",
                "ports": "0-65535",
                "source": "0.0.0.0/0",
            },
            {
                "protocol": "ICMP",
                "ports": "ALL",
                "source": "0.0.0.0/0",
            },
        ],
        "outbound_rules": [
            {
                "protocol": "ALL",
                "ports": "ALL",
                "destination": "0.0.0.0/0",
            },
        ],
    }

    print("=" * 60)
    print("  SECURITY GROUP OPEN TO THE WORLD CREATED")
    print("=" * 60)
    print(json.dumps(summary, indent=2))

    # ------------------------------------------------------------------
    # Security warning
    # ------------------------------------------------------------------
    print("\n" + "!" * 60)
    print("  ⚠️  SECURITY WARNING")
    print("!" * 60)
    print("  This security group allows ALL traffic from the entire internet.")
    print("  This is a significant security risk and should NEVER be used")
    print("  in production environments.")
    print()
    print("  To remediate:")
    print("   - Restrict inbound rules to specific IP ranges (e.g., your office CIDR).")
    print("   - Only open the specific ports required (e.g., 22 for SSH, 443 for HTTPS).")
    print("   - Consider using AWS Security Groups with least-privilege principles.")
    print()
    print(f"  To delete this security group, run:")
    print(f"    $ aws ec2 delete-security-group --group-id {group_id}")

    return summary


if __name__ == "__main__":
    # Allow an optional custom group name passed as a command-line argument
    name = sys.argv[1] if len(sys.argv) > 1 else "OpenToWorldSG"
    open_security_group(name)