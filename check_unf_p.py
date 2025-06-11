import json
import streamlit as st

st.title("📊 Instagram Unfollowers Checker")

st.markdown("Upload your **following** and **followers** JSON exports below.")

uploaded_following = st.file_uploader("Choose following.json", type="json")
uploaded_followers = st.file_uploader("Choose followers.json", type="json")

def extract_usernames(data, key):
    # handle top-level list or dict
    entries = data.get(key) if isinstance(data, dict) else data
    names = set()
    for e in entries or []:
        for item in e.get("string_list_data", []):
            if "value" in item:
                names.add(item["value"])
    return names

if uploaded_following and uploaded_followers:
    follow_data = json.load(uploaded_following)
    follower_data = json.load(uploaded_followers)

    following   = extract_usernames(follow_data, "relationships_following")
    followers   = extract_usernames(follower_data, "relationships_followed_by")
    unfollowers = sorted(following - followers)

    st.success(f"These accounts DO NOT follow you back:")
    st.write(unfollowers)

