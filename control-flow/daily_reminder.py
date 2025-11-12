task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# While loop to ensure user entered valid priority
while priority not in ["high", "medium", "low"]:
    priority = input("Please enter a valid priority (high/medium/low): ").strip().lower()
match priority:
    case "high":
        reminder = f"{task} is a high priority task"
    case "medium":
        reminder = f"{task} is a medium priority task"
    case "low":
        reminder = f"{task} is a low priority task"

if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder = f"Note: {reminder}. Consider completing it when you have free time." 
print(f"Reminder: {reminder}")