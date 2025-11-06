# Simple Bug Detector - Rule Based Version

def detect_bugs(code):
    bugs = []

    # Rule 1: Check for missing semicolons in C/C++
    if ("int" in code or "float" in code or "return" in code) and ";" not in code:
        bugs.append("Possible missing semicolon.")

    # Rule 2: Check for unmatched parentheses
    if code.count("(") != code.count(")"):
        bugs.append("Unmatched parentheses detected.")

    # Rule 3: Check for incorrect indentation (Python-like structure)
    lines = code.split("\n")
    for line in lines:
        if line.startswith(" ") and (len(line) - len(line.lstrip(" "))) % 4 != 0:
            bugs.append("Inconsistent indentation detected.")

    # Rule 4: Check print syntax for Python2 vs Python3 issue
    if "print " in code and "print(" not in code:
        bugs.append("Use print() instead of print statement (Python3 compatibility).")

    return bugs


# Example Run
user_code = input("Enter your code:\n")
issues = detect_bugs(user_code)

if len(issues) == 0:
    print("✅ No common issues found!")
else:
    print("⚠ Possible Issues:")
    for issue in issues:
        print("-", issue)
