"""Weekly privacy tip generator (Capstone 6, step 9).
Run:  python3 weekly_tip.py          -> prints a tip and saves weekly_tip.txt
"""
import datetime, pathlib

TIPS = [
    ('Review app permissions every month and remove any an app does not need', 'Apps only need data for their stated purpose.'),
    ('Use a unique password and two-step verification for email and banking', 'A hacked email account gives access to everything else.'),
    ('Read the purpose line before giving consent on any form', 'Consent must be informed, so know what you are saying yes to.'),
    ('Untick pre-ticked marketing and sharing boxes', 'Consent needs a clear action from you.'),
    ('Share Aadhaar only where it is truly required, and use a masked copy', 'Give the least sensitive ID that works.'),
    ('Keep location off unless an app needs it right now', 'Location shows where you live, study and travel.'),
    ('Never paste real personal data into AI chatbots', 'Prompts may be stored; use made-up examples.'),
    ('Avoid public Wi-Fi for banking and logins', 'Open networks are easier to snoop on.'),
    ('Report scams or breaches to the company, and cyber incidents to CERT-In', 'Quick reports limit the damage.'),
    ('Ask apps to delete your data when you stop using them', 'Uninstalling does not delete what the company holds. Use your right to erasure.'),
]

def tip_for(day=None):
    day = day or datetime.date.today()
    week = day.isocalendar()[1]
    return week, TIPS[(week - 1) % len(TIPS)]

def draft(day=None):
    week, (tip, why) = tip_for(day)
    return ("Privacy tip of the week (Week %d)\n\n%s.\n\nWhy it matters: %s\n\n"
            "Your data, your rights. Learn more on the DPDP awareness website." % (week, tip, why))

if __name__ == "__main__":
    text = draft()
    print(text)
    pathlib.Path("weekly_tip.txt").write_text(text, encoding="utf-8")
