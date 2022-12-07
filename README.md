# Instagram Followers vs Follows

## You can look who doesn't follow you

With the help of this program, you can see the difference between your follows and followers, and you can unfollow who doesn't follows you.

## How to use?

1. You should write your account informations here. Your accounts 2FA must be closed.

```sh
loader.login("USERNAME", "PASSWORD")
```

2. You should write your target account that you want to see followers and following.

```sh
profile = instaloader.Profile.from_username(loader.context,'USERNAME-OF-TARGET-PROFILE')
```

## Conclusion

You will get the difference between followers and following. People who doesn't follows you but you follow them will printed.
