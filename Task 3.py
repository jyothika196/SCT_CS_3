import tkinter as tk
import re

def check_strength():
    password = entry.get()
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("At least 8 characters")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letter")

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letter")

    # Number check
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add number")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special character")

    # Strength Result
    if score == 5:
        result_label.config(text="Strong Password 💪", fg="green")
    elif score >= 3:
        result_label.config(text="Medium Password 🙂", fg="orange")
    else:
        result_label.config(text="Weak Password 😟", fg="red")

    if feedback:
        suggestion_label.config(text="Suggestions: " + ", ".join(feedback))
    else:
        suggestion_label.config(text="Great job! Your password is secure.")

# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x250")

tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack(pady=10)

entry = tk.Entry(root, show="*", width=30)
entry.pack(pady=5)

tk.Button(root, text="Check Strength", command=check_strength).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=5)

suggestion_label = tk.Label(root, text="", wraplength=350)
suggestion_label.pack(pady=5)

root.mainloop()
