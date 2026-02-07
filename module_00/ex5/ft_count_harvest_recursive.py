def ft_count_harvest_recursive(total_day: int = None, day: int = 1) -> None:
    if total_day is None:
        total_day = int(input("Days until harvest: "))
    if total_day < day:
        print("Harvest time!")
        return
    print(f"Day {day}")
    ft_count_harvest_recursive(total_day, day + 1)
