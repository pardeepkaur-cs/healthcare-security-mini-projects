from datetime import datetime

# -------------------------------
# Synthetic Login Event Data
# -------------------------------

login_events = [
    {
        "user_id": "U1023",
        "role": "doctor",
        "login_time": "02:15",
        "ip_address": "192.168.1.45",
        "device_id": "DEV_009",
        "failed_attempts": 3,
        "password_strength": "weak",
        "known_ip": False,
        "known_device": False
    },
    {
        "user_id": "U2041",
        "role": "nurse",
        "login_time": "10:30",
        "ip_address": "192.168.1.12",
        "device_id": "DEV_002",
        "failed_attempts": 0,
        "password_strength": "strong",
        "known_ip": True,
        "known_device": True
    },
    {
        "user_id": "U3007",
        "role": "admin",
        "login_time": "23:10",
        "ip_address": "10.0.0.88",
        "device_id": "DEV_011",
        "failed_attempts": 2,
        "password_strength": "medium",
        "known_ip": False,
        "known_device": True
    },
    {
        "user_id": "U4112",
        "role": "doctor",
        "login_time": "19:40",
        "ip_address": "192.168.1.33",
        "device_id": "DEV_004",
        "failed_attempts": 1,
        "password_strength": "medium",
        "known_ip": True,
        "known_device": True
    },
    {
        "user_id": "U5220",
        "role": "nurse",
        "login_time": "04:55",
        "ip_address": "172.16.0.19",
        "device_id": "DEV_014",
        "failed_attempts": 4,
        "password_strength": "weak",
        "known_ip": False,
        "known_device": False
    }
]

NORMAL_START = 8
NORMAL_END = 20

def is_odd_hour(login_time_str):
    login_time = datetime.strptime(login_time_str, "%H:%M")
    hour = login_time.hour
    return hour < NORMAL_START or hour >= NORMAL_END

def classify_risk(score):
    if score >= 60:
        return "HIGH RISK"
    elif 35 <= score < 60:
        return "MEDIUM RISK"
    else:
        return "LOW RISK"

def evaluate_login_risk(event):
    risk_score = 0
    reasons = []

    if is_odd_hour(event["login_time"]):
        risk_score += 25
        reasons.append("Login outside normal hours (+25)")

    if not event["known_ip"]:
        risk_score += 30
        reasons.append("New IP address detected (+30)")

    if not event["known_device"]:
        risk_score += 20
        reasons.append("New device detected (+20)")

    if event["failed_attempts"] >= 2:
        risk_score += 15
        reasons.append("Multiple failed login attempts (+15)")

    if event["role"] == "admin":
        risk_score += 20
        reasons.append("Admin account sensitivity (+20)")
    elif event["role"] == "doctor":
        risk_score += 10
        reasons.append("Doctor account sensitivity (+10)")

    if event["password_strength"] == "weak":
        risk_score += 15
        reasons.append("Weak password (+15)")
    elif event["password_strength"] == "medium":
        risk_score += 5
        reasons.append("Medium-strength password (+5)")

    risk_level = classify_risk(risk_score)
    return risk_score, risk_level, reasons

def main():
    print("\n--- Healthcare Login Risk Scoring Report ---\n")

    for event in login_events:
        score, level, reasons = evaluate_login_risk(event)

        print(f"Login Event: {event['user_id']} ({event['role']})")
        print(f"Login Time: {event['login_time']}")
        print(f"Risk Score: {score} → {level}")

        if reasons:
            print("Reasons:")
            for r in reasons:
                print(f" - {r}")
        else:
            print("Reasons:")
            print(" - No significant anomalies detected")

        print("-" * 50)

    print("\nEnd of report.\n")

if __name__ == "__main__":
    main()
