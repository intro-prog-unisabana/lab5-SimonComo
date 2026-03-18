# debugging.py
def total_steps(steps):
    return sum(steps)

def average_steps(steps):
    return sum(steps) // len(steps)

def max_steps(steps):
    return max(steps)

def min_steps(steps):
    return min(steps)

def goal_met(steps):
    return [step >= 10000 for step in steps]

entrada = input()
steps = list(map(int, entrada.split()))

print("Total steps:", total_steps(steps))
print("Average daily steps:", average_steps(steps))
print("Highest steps in a day:", max_steps(steps))
print("Lowest steps in a day:", min_steps(steps))
print("Goal met each day:", goal_met(steps))