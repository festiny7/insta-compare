import instaloader

loader = instaloader.Instaloader()
loader.login("USERNAME", "PASSWORD")
profile = instaloader.Profile.from_username(
    loader.context, "USERNAME-OF-TARGET-PROFILE"
)


followers = profile.get_followers()

followers_list = []

for follower in followers:
    followers_list.append(str(follower))

follows = profile.get_followees()

follows_list = []

for follow in follows:
    follows_list.append(str(follow))

res = [x for x in follows_list if x not in followers_list]

print(res)
