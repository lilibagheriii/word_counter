import re

def extract_emails(text):
    # Regex pattern for basic email
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return re.findall(pattern, text)

if __name__ == "__main__":
    sample = """
    Contact us at support@example.com or sales@company.co.uk.
    You can also reach mary_jane123@gmail.com!
    """
    emails = extract_emails(sample)
    print("Found emails:")
    for email in emails:
        print("-", email)
