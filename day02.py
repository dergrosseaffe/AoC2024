def is_safe(report, can_skip_one = False):
    if len(report) < 2:
        return True
    
    previous = report[0]
    increasing = report[1] >= previous
    
    for current in report[1:]:
        diff = abs(current - previous)
        if diff < 1 or diff > 3:
            if can_skip_one:
                can_skip_one = False
                continue
            else:
                return False

        if increasing and current < previous:
            if can_skip_one:
                can_skip_one = False
                continue
            else:
                return False
        if not increasing and current > previous:
            if can_skip_one:
                can_skip_one = False
                continue
            else:
                return False
        
        previous = current

    return True


safe = 0
safe_skip_one = 0
while True:
    try: report = [int(level) for level in input().split()]
    except EOFError: break

    safe += 1 if is_safe(report) else 0
    safe_skip_one += 1 if is_safe(report, True) else 0

print(safe)
print(safe_skip_one)