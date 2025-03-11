def compute(n):
    n1 = int(f"{n}")
    n2 = int(f"{n}{n}")
    n3 = int(f"{n}{n}{n}")
    n4 = int(f"{n}{n}{n}{n}")
    return n1 + n2 + n3 + n4

for i in range(4, 8):
    print(f"compute({i}) = {compute(i)}")    