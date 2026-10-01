These YAML files are GitHub Actions workflow drafts.

Move each file to `.github/workflows/` for GitHub Actions to recognize them.
The GitHub MCP token lacked the Workflows write permission, so they could not be placed there directly.

Required repo secrets for AWS workflows:
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_REGION
