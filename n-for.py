num = int(input())
n = 0

for l1 in range(1,4):
    if l1 == num:
        n += 1
    for l2 in range(1,4):
        if l1 + l2 == num:
            n += 1
        for l3 in range(1,4):
            if l1 + l2 + l3 == num:
                n += 1
            for l4 in range(1,4):
                if l1 + l2 + l3 + l4 == num:
                    n += 1
                for l5 in range(1,4):
                    if l1 + l2 + l3 + l4 + l5 == num:
                        n += 1
                    for l6 in range(1,4):
                        if l1 + l2 + l3 + l4 + l5 + l6 == num:
                            n += 1
                        for l7 in range(1,4):
                            if l1 + l2 + l3 + l4 + l5 + l6 + l7 == num:
                                n += 1
                            for l8 in range(1,4):
                                if l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8 == num:
                                    n += 1
                                for l9 in range(1,4):
                                    if l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8 + l9 == num:
                                        n += 1
                                    for l10 in range(1,4):
                                        if l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8 + l9 + l10 == num:
                                            n += 1

print(n)