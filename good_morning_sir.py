import time

# Get current hour as an integer
hour = int(time.strftime('%H'))

print("Current Hour:", hour)

# Check time range
if 4 <= hour < 12:
    print("Good Morning")
elif 12 <= hour < 16:
    print("Good Afternoon")
elif 16 <= hour < 20:
    print("Good Evening")
else:
    print("Good Night")
