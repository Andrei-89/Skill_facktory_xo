a = "1234"

def digital_root(n):
    n = " ".join(n).split()
    n = list(map(int, n))
    if len(n) == 1:
        n = str(sum(n))
        return digital_root(n)

print(digital_root(a))
