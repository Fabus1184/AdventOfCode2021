import sys

print("INPUT:")
kek = sys.stdin.readlines()

print("{")

for k in kek:
    if k == "\n":
        continue
    if "---" in k:
        print("},{")
    else:
        print("{%s}," % k.replace("\n", ""))

print("}")
