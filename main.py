"""Run this to see who you're following that doesn't follow you back."""
import json
from typing import Any

with open("followers_1.json", "r", encoding="utf-8") as f:
    followers_data: list[dict[str, Any]] = json.load(f)
followers: set[str] = {user["string_list_data"][0]["value"] for user in followers_data}

with open("following.json", "r", encoding="utf-8") as f:
    following_data: dict[str, list[dict[str, Any]]] = json.load(f)
following: set[str] = {user["title"] for user in following_data["relationships_following"]}

not_following_back: set[str] = following - followers

print(f"You follow {len(following)} people.")
print(f"{len(not_following_back)} do not follow you back:")
for user in sorted(not_following_back):
    print("•", user)