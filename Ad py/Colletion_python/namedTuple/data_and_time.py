from datetime import datetime

# Get the current date and time
now = datetime.now()

# Format the date and time
current_time = now.strftime("%Y-%m-%d %H:%M:%S")
print("Current Date and Time:", current_time)

# Parse a string into a datetime object
date_string = "2024-10-25 22:23:00"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("Parsed Date and Time:", parsed_date)
