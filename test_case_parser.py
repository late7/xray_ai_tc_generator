# test_case_parser.py
import json
import re

def process_test_case(test_case_text):
    lines = test_case_text.strip().split('\n')
    test_case_number = re.findall(r'\d+', lines[0])[0]
    description = lines[1].split("Description:", 1)[1].strip()

    steps = []
    for line in lines[3:]:  # Exclude the "Test steps:" line and before
        if line:
            step_split = line.split('.', 1)
            if len(step_split) == 2:
                _, step_text = step_split
                steps.append({
                    "action": step_text.strip(),
                    "data": "",
                    "result": ""
                })

    return {
        "testtype": "Manual",
        "fields": {
            "summary": f"Test Case {test_case_number}: {description}",
            "description": ""
        },
        "steps": steps
    }

def text_to_json(input_text):
    # Split the input text into individual test cases and process them
    test_cases = [process_test_case(tc) for tc in input_text.strip().split('Test Case') if tc]

    # Convert the test cases to JSON
    return json.dumps(test_cases, indent=4)

def filter_test_cases(json_data):
    # Parse the JSON data
    test_cases = json.loads(json_data)

    # Display the available test cases
    print("Available Test Cases:")
    for index, test_case in enumerate(test_cases, start=1):
        summary = test_case["fields"]["summary"]
        print(f"{index}. {summary}")
    print("Press Enter to keep all test cases or enter specific numbers to select (e.g., 1,3).")

    # Ask user which test cases to keep
    selected_indices = input("Make your selection: ").strip()
    
    # If the user just hits Enter, assume 'all' is selected
    if not selected_indices:
        return json_data

    # Otherwise, process the user's input
    selected_indices = [int(i) for i in selected_indices.split(',') if i.isdigit()]

    # Filter the test cases based on user selection
    filtered_test_cases = [test_cases[i - 1] for i in selected_indices if 0 < i <= len(test_cases)]

    # Convert the filtered test cases back to JSON
    return json.dumps(filtered_test_cases, indent=4)


