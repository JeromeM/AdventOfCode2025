with open("input.txt") as f:
    input = f.read()
# input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
output = 0

for product in input.split(","):
    start, end = map(int, product.split("-"))
    for pid in range(start, end + 1):
        p = str(pid)
        left = str(p[0:len(str(p))//2])
        right = str(p[len(str(p))//2:])
        if left == right:
            output += pid

print(f"Output: {output}")