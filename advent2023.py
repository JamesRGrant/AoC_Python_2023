import day01


def main():
    with open("input\\01.txt", "r") as file:
        lines = file.read().splitlines()

    print("Day 1:")
    print("   p1: " + str(day01.p1(lines)))
    print("   p2: " + str(day01.p2(lines)))


if __name__ == "__main__":
    main()
