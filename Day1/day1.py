val = 50
password1 = 0
password2 = 0

with open("input.txt") as f:
    seq = tuple(line.strip() for line in f)

# seq = ("L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82")

for s in seq:
    for i in range(1, int(s[1:]) + 1):
        if s[0:1] == "L":
            val = (100 if val == 0 else val)
            password2 = (password2 + 1) if val == 100 else password2
            val -= 1
        else:
            val = (0 if val == 100 else val)
            password2 = (password2 + 1) if val == 0 else password2
            val += 1
    
    if val == 0 or val == 100:
        password1 += 1

print(f"Password 1: {password1}")
print(f"Password 2: {password2}")