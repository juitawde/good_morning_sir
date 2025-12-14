# ⏰ Time-Based Greeting Program (Python)

A simple **Python program** that displays a greeting message based on the **current system time**.  
The greeting changes automatically depending on the hour of the day.

---

## 📌 Project Description

This program uses Python’s built-in `time` module to:
- Fetch the current hour from the system
- Determine the time of day
- Display an appropriate greeting:
  - Good Morning
  - Good Afternoon
  - Good Evening
  - Good Night

---

## 🕒 Greeting Logic

| Time Range (24-hour) | Greeting |
|--------------------|----------|
| 04:00 – 11:59 | Good Morning |
| 12:00 – 15:59 | Good Afternoon |
| 16:00 – 19:59 | Good Evening |
| 20:00 – 03:59 | Good Night |

---

## ▶️ How to Run the Program

1. Make sure **Python** is installed on your system
2. Save the file as:
```

time_greeting.py

```
3. Open terminal / command prompt
4. Run the program:
```

python time_greeting.py

```

---

## 🧾 Sample Output

```

Current Hour: 10
Good Morning

```

---

## 🛠️ Concepts Used

- Python `time` module
- Conditional statements (`if-elif-else`)
- System time handling
- Integer conversion

---

## 🚀 Possible Enhancements

- Display current date along with time
- Add personalized greeting with user name
- Support different time zones
- Use `datetime` module instead of `time`

---

## 👩‍💻 Author

Python Beginner Practice Program  
Created to understand **time-based conditions** 🐍

---

⭐ Feel free to star the repository if you found this useful!
