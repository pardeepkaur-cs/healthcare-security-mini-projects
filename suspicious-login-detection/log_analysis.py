This project demonstrates a simple rule-based approach to detecting suspicious login behavior in a hospital information system using synthetic data.

It applies interpretable rules such as repeated failed login attempts, unusual login times, and access from multiple locations to flag potentially concerning access patterns.

This project is intended for academic illustration only and does not use real hospital data.
#Rule-Based Suspicious Login Detection
# Academic illustration only

import pandas as pd
from datetime import datetime

data = {
    "user_id": ["U101", "U101", "U101", "U101", "U102", "U102", "U103", "U103"],
    "timestamp": [
        "2026-01-01 09:00", "2026-01-01 09:02", "2026-01-01 09:04", "2026-01-01 09:06",
        "2026-01-01 00:30", "2026-01-01 00:35",
        "2026-01-01 14:00", "2026-01-01 14:03"
    ],
    "location": ["Delhi", "Delhi", "Delhi", "Delhi", "Mumbai", "Mumbai", "Chennai", "Bangalore"],
    "login_status": ["failed", "failed", "failed", "failed", "success", "success", "success", "success"]
}

df = pd.DataFrame(data)
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Rule 1: Repeated failed logins
failed_logins = df[df["login_status"] == "failed"]
failed_counts = failed_logins.groupby("user_id").size()
suspicious_failed_users = failed_counts[failed_counts > 3]

# Rule 2: Unusual hours
df["login_hour"] = df["timestamp"].dt.hour
late_night_logins = df[(df["login_hour"] >= 0) & (df["login_hour"] <= 5)]

# Rule 3: Multiple locations
df_sorted = df.sort_values(by=["user_id", "timestamp"])

multi_location_users = []
for user in df_sorted["user_id"].unique():
    user_records = df_sorted[df_sorted["user_id"] == user]
    if user_records["location"].nunique() > 1:
        multi_location_users.append(user)

print("Users with excessive failed logins:")
print(suspicious_failed_users)

print("\nLate night logins:")
print(late_night_logins[["user_id", "timestamp", "location"]])

print("\nUsers with multiple login locations:")
print(multi_location_users)
