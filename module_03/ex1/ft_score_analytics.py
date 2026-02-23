import sys

def display_scors(scors: list[int]) -> None:
    print("Scores processed: [", end="")
    i = 0
    while i < len(scores):
        if i:
            print(", ", end="")
        print(scores[i], end="")
        if i == len(scores) - 1:
            print("]")
        i += 1




if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    if len(sys.argv) > 1:
        scores: list[int] = []
        i = 1
        while i < len(sys.argv):
            scores.append(int(sys.argv[i]))
            i += 1
        display_scors(scores)
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores, 0) / len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")

    else:
        print("No scores provided. Usage: python3",
              f"{sys.argv[0]} <score1> <score2> ...")
