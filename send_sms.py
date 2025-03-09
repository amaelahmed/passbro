from twilio.rest import Client

# Twilio credentials (Replace with your actual details)
account_sid = "ACda096e4697507203391a3d7383077e5d"
auth_token = "e2d3bc96e86df42cf531bcea6d6fc3f7"
twilio_number = "+12515124558"
target_number = "+918921551882"

# Create Twilio client
client = Client(account_sid, auth_token)

# Send a test SMS
message = client.messages.create(
    body="🔴 Security Alert: SIM toolkit update required. Reply 'YES' to proceed.",
    from_=twilio_number,
    to=target_number
)

print(f"✅ Message sent! SID: {message.sid}")
