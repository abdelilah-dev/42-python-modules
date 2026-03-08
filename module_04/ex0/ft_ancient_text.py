def ft_ancient_text() -> None:
    try:
        print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
        file_name = "ancient_fragment.txt"
        print(f"\nAccessing Storage Vault: {file_name}")
        file = open(file_name, 'r')
        print("Connection established...\n")
        try:
            content = file.read()
            print("RECOVERED DATA:")
            print(content)
            print("\nData recovery complete. Storage unit disconnected.")
        except OSError as error:
            print(f"Failed Reading File: {error}")
        finally:
            file.close()
    except (FileNotFoundError, PermissionError, OSError, ValueError) as error:
        print(f"Failed To Accessing Storage Vault: {error}")


if __name__ == "__main__":
    ft_ancient_text()
