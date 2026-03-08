import sys


def display_op_status(status) -> None:
    try:
        if status == "success":
            print("STATUS: Normal operations resumed")
        elif status == "permission_deny":
            print("STATUS: Crisis handled, security maintained")
        else:
            print("STATUS: Crisis handled, system stable")
    except OSError as error:
        print(f"Failed To Displaying Operation Status: {error}",
              file=sys.stderr)


def try_to_access(file_name: str) -> str:
    try:
        print(f"\nCRISIS ALERT: Attempting access to '{file_name}'...")
        with open(file_name, 'r') as file:
            content = file.read()
            print(f"SUCCESS: Archive recovered - ``{content}``")
        return "success"
    except PermissionError:
        print("RESPONSE: Security protocols deny access",
              file=sys.stderr)
        return "permission_deny"
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix",
              file=sys.stderr)
        return "not_found"
    except (OSError, ValueError) as error:
        print(f"RESPONSE: {error}", file=sys.stderr)


def ft_crisis_response():
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    try:
        files = [
            "lost_archive.txt",
            "classified_vault.txt",
            "standard_archive.txt"
        ]
        for file in files:
            status = try_to_access(file)
            display_op_status(status)
        print("\nAll crisis scenarios handled successfully. Archives secure.")
    except (OSError, ValueError) as error:
        print(f"The Big Crisis: {error}", file=sys.stderr)


if __name__ == "__main__":
    ft_crisis_response()
