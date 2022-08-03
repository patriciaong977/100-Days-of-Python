def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True # Leap Year = True
      else:
        return False  # Not a Leap Year = False
    else:
      return True # Leap Year = True
  else:
    return False  # Not a Leap Year = False

# Need to know the number of days in each month.
def days_in_month(year, month):  # year and month parameter
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  # Checking if month input is valid.
  if month > 12 or month < 1:
    return "Invalid Month"

  # Check if year is a leap
  if is_leap(year) and month == 2: # Can call a function within a function.
    return 29 # 29 days in February.
  else:
    return month_days[month - 1] # Index starts at 0.

#🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
