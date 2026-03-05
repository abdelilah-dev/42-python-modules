import sys


def display(list: list[any]) -> None:
    i = 0
    for ele in list:
        if i != 0:
            print(", ", end="")
        print(ele, end="")
        i += 1
    print("")


def create_dictionary(usr_input: list[str]) -> None:
    dict_created: dict = dict()
    try:
        for item in usr_input:
            key, value = item.split(":")
            dict_created[key] = int(value)
        return dict_created
    except Exception as error:
        raise ValueError(f"Error Creating Dictionary : {error}")


def get_total_values(dic: dict) -> int:
    total = 0
    for value in dic.values():
        total += value
    return total


def get_percent_of_ele(value: int, total: int) -> float:
    return round(((value * 100) / total), 1)


def display_curr_inventory(dic: dict) -> None:
    for key in dic.keys():
        print(f"{key}: {dic[key]} units",
              f"({get_percent_of_ele(dic[key], get_total_values(dic))}%)")


def get_big_value(dic: dict) -> list:
    big_val = ["", -999]
    for ele in dic:
        if dic[ele] > big_val[1]:
            big_val[1] = dic[ele]
            big_val[0] = ele
    return (big_val)


def get_small_value(dic: dict) -> list:
    sml_val = ["", 999]
    for ele in dic:
        if dic[ele] < sml_val[1]:
            sml_val[1] = dic[ele]
            sml_val[0] = ele
    return (sml_val)


def get_moderate_item(dic: dict) -> dict:
    moderate: dict = dict()
    for ele in dic:
        if get_percent_of_ele(dic[ele],
                              get_total_values(dic)) > 100 / len(dic):
            moderate[ele] = dic[ele]
    return (moderate)


def get_scarce_item(dic: dict) -> dict:
    moderate: dict = dict()
    for ele in dic:
        if get_percent_of_ele(dic[ele],
                              get_total_values(dic)) < 100 / len(dic):
            moderate[ele] = dic[ele]
    return (moderate)


def lookup(dic: dict, key: str) -> None:
    print(f"Sample lookup - '{key}' in inventory:",
          f"{"False" if (dic.get(key) is None) else "True"}")


if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            del sys.argv[0]
            dic = create_dictionary(sys.argv)

            print("=== Inventory System Analysis ===")
            print(f"Total items in inventory: {get_total_values(dic)}")
            print(f"Unique item types: {len(dic)}")

            print("\n=== Current Inventory ===")
            display_curr_inventory(dic)

            print("\n=== Inventory Statistics ===")
            big_ele = get_big_value(dic)
            sml_ele = get_small_value(dic)
            print(f"Most abundant: {big_ele[0]} ({big_ele[1]} units)")
            print(f"Least abundant: {sml_ele[0]} ({sml_ele[1]} unit)")

            print("\n=== Item Categories ===")
            moderate = get_moderate_item(dic)
            print(f"Moderate: {moderate}")
            scarce = get_scarce_item(dic)
            print(f"Scarce: {scarce}")

            print("\n=== Management Suggestions ===")
            print("Restock needed: ", end="")
            display(scarce.keys())

            print("\n=== Dictionary Properties Demo ===")
            print("Dictionary keys: ", end="")
            display(dic.keys())
            print("Dictionary values: ", end="")
            display(dic.values())
            lookup(dic, "sword")
        else:
            raise ValueError("please enter valid argument \"key:value\"")
    except Exception as error:
        print(f"\033[31m{error}\033[0m")
        1350
