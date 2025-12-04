seq = ("987654321111111",
       "811111111111119",
       "234234234234278",
       "818181911112111")

with open("input.txt") as f:
    seq = tuple(line.strip() for line in f)

def part1() -> int:
    total: int = 0
    for s in seq:
        best = 0
        for i, a in enumerate(s):
            for b in s[i+1:]:
                best = max(best, int(a + b))
        total += best
    return total

def part2() -> int:
    total: int = 0
    for s in seq:
        total += max_number(s)
    return total

def max_number(line: str, k: int=12) -> int:
    result: list = []
    start: int = 0
    for remaining in range(k, 0, -1):
        end = len(line) - remaining + 1
        best_idx = max(range(start, end), key=lambda i: line[i])
        result.append(line[best_idx])
        start = best_idx + 1
    return int(''.join(result))

print(f"Output part 1: {part1()}")
print(f"Output part 2: {part2()}")
