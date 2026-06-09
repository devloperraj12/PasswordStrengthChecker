import re
import math
from datetime import datetime

print("=" * 60)
print("          PASSWORD SECURITY ANALYZER")
print("=" * 60)

password = input("\nEnter Password: ")

masked = "*" * len(password)

score = 0
recommendations = []

breached_passwords = [
    "password",
    "password123",
    "123456",
    "123456789",
    "admin",
    "welcome",
    "qwerty",
    "letmein",
    "abc123"
]

# Length Check
if len(password) >= 12:
    score += 20
else:
    recommendations.append("Use at least 12 characters")

# Uppercase Check
if re.search(r"[A-Z]", password):
    score += 20
else:
    recommendations.append("Add uppercase letters")

# Lowercase Check
if re.search(r"[a-z]", password):
    score += 20
else:
    recommendations.append("Add lowercase letters")

# Number Check
if re.search(r"\d", password):
    score += 20
else:
    recommendations.append("Add numbers")

# Special Character Check
if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    score += 20
else:
    recommendations.append("Add special characters")

# Breached Password Detection
breached = False

if password.lower() in breached_passwords:
    breached = True
    score -= 30

if score < 0:
    score = 0

# Entropy Calculation
charset = 0

if re.search(r"[a-z]", password):
    charset += 26

if re.search(r"[A-Z]", password):
    charset += 26

if re.search(r"\d", password):
    charset += 10

if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    charset += 32

if charset > 0:
    entropy = len(password) * math.log2(charset)
else:
    entropy = 0

# Crack Time Estimation
if entropy < 28:
    crack_time = "Seconds"
elif entropy < 36:
    crack_time = "Minutes"
elif entropy < 60:
    crack_time = "Hours / Days"
elif entropy < 80:
    crack_time = "Years"
else:
    crack_time = "Thousands of Years"

# Strength Category
if score < 40:
    strength = "WEAK"
    grade = "D"
elif score < 70:
    strength = "MEDIUM"
    grade = "C"
elif score < 90:
    strength = "STRONG"
    grade = "B"
elif score < 100:
    strength = "VERY STRONG"
    grade = "A"
else:
    strength = "EXCELLENT"
    grade = "A+"

# Strength Meter
filled = score // 5
meter = "█" * filled + "░" * (20 - filled)

print("\n" + "=" * 60)
print("SECURITY ANALYSIS REPORT")
print("=" * 60)

print(f"Password Length      : {len(password)}")
print(f"Password Masked      : {masked}")
print(f"Security Score       : {score}/100")
print(f"Security Grade       : {grade}")
print(f"Password Entropy     : {entropy:.2f} bits")
print(f"Crack Time Estimate  : {crack_time}")

print("\n" + "-" * 60)
print("PASSWORD STRENGTH")
print("-" * 60)

print(f"{strength}")
print(f"\n[{meter}] {score}%")

print("\n" + "-" * 60)
print("SECURITY CHECKS")
print("-" * 60)

print("[✓] Uppercase Letters" if re.search(r"[A-Z]", password)
      else "[✗] Uppercase Letters")

print("[✓] Lowercase Letters" if re.search(r"[a-z]", password)
      else "[✗] Lowercase Letters")

print("[✓] Numbers" if re.search(r"\d", password)
      else "[✗] Numbers")

print("[✓] Special Characters"
      if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)
      else "[✗] Special Characters")

print("[✓] Length >= 12"
      if len(password) >= 12
      else "[✗] Length < 12")

if breached:
    print("\nWARNING!")
    print("This password appears in commonly breached password lists.")

print("\n" + "-" * 60)
print("RECOMMENDATIONS")
print("-" * 60)

if recommendations:
    for item in recommendations:
        print(f"➜ {item}")
else:
    print("No Security Issues Found.")

# Save Report
with open("password_report.txt", "w") as report:

    report.write("PASSWORD SECURITY REPORT\n")
    report.write("=" * 60 + "\n")
    report.write(f"Generated: {datetime.now()}\n\n")

    report.write(f"Password Length : {len(password)}\n")
    report.write(f"Security Score  : {score}/100\n")
    report.write(f"Security Grade  : {grade}\n")
    report.write(f"Strength        : {strength}\n")
    report.write(f"Entropy         : {entropy:.2f} bits\n")
    report.write(f"Crack Time      : {crack_time}\n\n")

    report.write("Recommendations:\n")

    if recommendations:
        for item in recommendations:
            report.write(f"- {item}\n")
    else:
        report.write("No Security Issues Found.\n")

print("\n" + "-" * 60)
print("REPORT GENERATED")
print("-" * 60)
print("Saved as: password_report.txt")
print("=" * 60)
