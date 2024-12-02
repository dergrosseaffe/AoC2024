def is_safe(report, can_skip_one = False):
    if len(report) < 2:
        return True
    
    def is_monotonic(subreport):
        previous = subreport[0]
        increasing = subreport[1] >= previous
        for current in subreport[1:]:
            diff = abs(current - previous)
            if diff < 1 or diff > 3:
                return False

            if increasing and current < previous:
                return False
            if not increasing and current > previous:
                return False
            
            previous = current

        return True
    
    if is_monotonic(report):
        return True
    
    if can_skip_one:
        for i in range(len(report)):
            if is_monotonic(report[:i] + report[i+1:]):
                return True
        
    return False


safe = 0
safe_skip_one = 0
while True:
    try: report = [int(level) for level in input().split()]
    except EOFError: break

    safe += 1 if is_safe(report) else 0
    safe_skip_one += 1 if is_safe(report, True) else 0

print(safe)
print(safe_skip_one)