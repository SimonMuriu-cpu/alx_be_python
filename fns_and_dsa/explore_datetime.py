from datetime import datetime, timedelta

def display_current_datetime():
    # Save the current date and time
    current_date = datetime.now()
    # Print formatted date and time
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date(days):
    # Save the future date
    future_date = datetime.now() + timedelta(days=days)
    # Print formatted future date
    print("Future date:", future_date.strftime("%Y-%m-%d"))


def main():
    # Part 1: Display current date and time
    display_current_datetime()

    # Part 2: Prompt user for days to add
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days_to_add)
    except ValueError:
        print("Invalid input. Please enter an integer number of days.")

if __name__ == "__main__":
    main()
