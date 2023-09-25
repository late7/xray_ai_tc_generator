# Python Script for Generating Test Cases

This Python script generates test cases for a given requirement specification using OpenAI's GPT-4 model and imports them into XRAY, a test management tool for Jira.

## Arguments

Example run command:
> python .\generate-tcs-for-issue.py --req TST-47 --username lasse@gmail.com --url https://test.atlassian.net

The script takes in the following arguments:

- `--req`: The ID of the Jira issue containing the requirement specification.
- `--username`: The username used to log in to Jira.
- `--url`: The URL of the Jira Cloud instance.
- `--debug`: A boolean flag indicating whether to print debug information.

## Workflow

1. Fetches the requirement data from Jira using the provided issue ID.
2. Generates test cases for the requirement using OpenAI's GPT-4 model.
3. Saves the output to a JSON file.
4. Imports the generated test cases into XRAY using the XRAY API.

## Libraries Used

- `requests`: To make HTTP requests to Jira and XRAY.
- `openai`: To interact with OpenAI's GPT-4 API.
- `argparse`: To parse command-line arguments.

## Example token and auth files

### Jira API token just one line:
eyJhbGciO1NiIsInR5cCI6IkpXVCJ9.eyJ0ZW5hbnQiOiIz...........

### OpenAI API token just one line:
sk-0NpOoHLtMASW5ECT3Blb..............

### XRAY Suth json also just one line
{ "client_id": "FF328C5A1A487E9A...........","client_secret": "bbf3997c59bb1d63e76658fd266414c73............" }
