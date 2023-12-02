from timer import Timer


@Timer(name="Day 1: Part 1")
def p1(input):
    sum = 0
    for line in input:
        tmp = ""
        for c in line:
            if c.isdigit():
                tmp += c
                break

        for c in line[::-1]:
            if c.isdigit():
                tmp += c
                break

        sum += int(tmp)

    return sum


@Timer(name="Day 1: Part 2")
def p2(input):
    sum = 0
    nums = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    for line in input:
        tmp = ""
        for i in range(len(line)):
            # check if digit
            if line[i].isdigit():
                tmp += line[i]
                break

            # check if word
            for j in range(len(nums)):
                if line[i::].find(nums[j]) == 0:
                    tmp += str(j)
                    break
            else:
                continue  # only executed if the inner loop did NOT break
            break  # only executed if the inner loop DID break

        for i in reversed(range(len(line))):
            # check if digit
            if line[i].isdigit():
                tmp += line[i]
                break

            # check if word
            for j in range(len(nums)):
                if line[i::].find(nums[j]) == 0:
                    tmp += str(j)
                    break
            else:
                continue  # only executed if the inner loop did NOT break
            break  # only executed if the inner loop DID break

        sum += int(tmp)

    return sum
