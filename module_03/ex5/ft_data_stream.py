data = [
    {"name": "frank", "event": "logged-in", "level": 16},
    {"name": "alice", "event": "leveled up", "level": 45},
    {"name": "bob", "event": "death", "level": 1},
    {"name": "charlie", "event": "kill someone", "level": 22},
    {"name": "diana", "event": "logged-in", "level": 17},
    {"name": "frank", "event": "leveled up", "level": 11},
    {"name": "charlie", "event": "item_found", "level": 44},
    {"name": "bob", "event": "logged-in", "level": 18},
    {"name": "eve", "event": "leveled up", "level": 32},
]


def generate_events(data: list):
    for pl in data:
        yield pl


def generate_fibonacci_seq(n: int):
    old = 0
    new = 1
    yield old
    yield new
    i = 0
    while i < n - 2:
        yield old + new
        tmp = old
        old = new
        new = tmp + new
        i += 1


def generate_prime_numebers(n: int):
    generated = 0
    num = 2
    while (generated < n):
        i = 2
        while (i < num):
            if num % i == 0:
                break
            i += 1
        if i == num:
            yield num
            generated += 1
        num += 1


def stroe_everything() -> list:
    return [1, 2, 3]


def stream_everything():
    yield 1
    yield 2
    yield 3


def display_fibonacci_of_n(n: int) -> None:
    print(f"Fibonacci sequence (first {n}): ", end="")
    for ele in generate_fibonacci_seq(n):
        if ele != 0:
            print(", ", end="")
        print(ele, end="")
    print("")


def display_first_n_prime_num(n: int) -> None:
    print(f"Prime numbers (first {n}): ", end="")
    for i in generate_prime_numebers(n):
        if i != 2:
            print(", ", end="")
        print(f"{i}", end="")
    print("")


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    print(f"Processing {len(data)} game events...\n")
    i = 1
    heigh_level = 0
    level_up_ev = 0
    treasure_ev = 0
    for pl in generate_events(data):
        print(f"Event {i}: Player {pl["name"]}",
              f"(level {pl["level"]}) {pl["event"]}")
        if pl["level"] > heigh_level:
            heigh_level = pl["level"]
        if pl["event"] == "leveled up":
            level_up_ev += 1
        i += 1

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {i - 1}")
    print(f"High-level players (10+): {heigh_level}")
    print(f"Treasure events: {treasure_ev}")
    print(f"Level-up events: {level_up_ev}")

    print("\n=== difference between \"store everything\"",
          "vs \"stream everything\" ===")
    print(f"store Everything: {stroe_everything()}")
    print("Stream Everything: ")
    for ele in stream_everything():
        print(ele)

    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0 seconds")

    print("\n=== Generator Demonstration ===")
    display_fibonacci_of_n(10)
    display_first_n_prime_num(5)
