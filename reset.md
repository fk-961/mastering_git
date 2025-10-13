A very useful tool/command is the <code>git reset commit_hash</code> command. (Use <code>git log</code> to get the commits hashes).
If reset is used without a hash the default parameter is the current commit.

## There are 3 types of resets:
- **mixed reset**: used when executing get reset without options. It goes back to the speicified commit without staging all the changes that we did after that commit. This way we can modify the code if we want and then stage and commit the changes that we made.
- **soft reset**: used with the option "soft". It goes back to the specified commit and stages the changes made after that commit. I think this is used to reduce the number of commits that we made while developing a feature to not push a lot of commits.
- **hard reset**: used with the option "hard". It goes back to the specified commit and disgards all the changes made after that commit. We won't be able to see any changes made after that commit in our working directory.