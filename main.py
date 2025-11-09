"""Run script."""
import json

# Load followers
with open("followers_1.json", "r", encoding="utf-8") as f:
    followers_data = json.load(f)
followers = {user["string_list_data"][0]["value"] for user in followers_data}

# Load following
with open("following.json", "r", encoding="utf-8") as f:
    following_data = json.load(f)
following = {user["string_list_data"][0]["value"] for user in following_data["relationships_following"]}

# Compute non-followers
not_following_back = following - followers

print(f"You follow {len(following)} people.")
print(f"{len(not_following_back)} do not follow you back:")
for user in sorted(not_following_back):
    print("•", user)
