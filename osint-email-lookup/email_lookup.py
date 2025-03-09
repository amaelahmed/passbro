import os

print("🔍 Performing OSINT email lookup...")

email = input("Enter the email to search: ")

# Basic Google Dorking
google_dork = f"https://www.google.com/search?q={email}"
print(f"🔗 Try searching here: {google_dork}")

# Check breach data using Holehe (no API key required)
print("\n🔍 Checking for data breaches...\n")
os.system(f"holehe {email}")

# Check social media accounts using Sherlock
print("\n🔍 Checking social media accounts...\n")
os.system(f"python3 -m sherlock {email}")

