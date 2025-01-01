import jwt
import datetime

def generate_token():
    payload = {
        "iss":"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" ,  # Replace with your API key ID
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
        "video": {
            "roomCreate": True,
            "roomJoin": True,
            "roomList": True,
            "roomRecord": True,
            "roomAdmin": True
        },
        "identity": "Abhinay"  # Replace with your user identity
    }
    token = jwt.encode(payload, "VfmvNvfRyPellVH2LF7ebcyeJI7hZZJPm3eTlZ9h8ifG", algorithm="HS256")  # Replace with your API key secret
    return token

# Print the new token
print(generate_token())
