def write_data_to_file(file, data: list[str]) -> None:
    print("Inscribing preservation data...")
    for text in data:
        print(text, end="")
        file.write(text)
    print("\nData inscription complete. Storage unit sealed.")


def ft_archive_creation() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    file_name = "new_discovery.txt"
    data = [
        "[ENTRY 001] New quantum algorithm discovered\n",
        "[ENTRY 002] Efficiency increased by 347%\n"
        "[ENTRY 003] Archived by Data Archivist trainee\n"
    ]
    try:
        print(f"\nInitializing new storage unit: {file_name}")
        file = open(file_name, 'w')
        print("Storage unit created successfully...\n")
        try:
            write_data_to_file(file, data)
            print(f"Archive '{file_name}' ready for long-term preservation.")
        except (OSError, ValueError) as error:
            print(f"Failed To Write in File: {error}")
        finally:
            file.close()
    except (OSError, ValueError) as error:
        print(f"Failed To Open a File: {error}")


if __name__ == "__main__":
    ft_archive_creation()
