# GithubUserInfo

This package is only for Github Public User's Account.

## Installation of Package
```bash
$ pip install GithubUserInfo
```

## Simple Demo

```python
# import the package
from GithubUserInfo import githubUserAccount as gt

# using username get details of github account
gt.get("username")

# using username set the username & call other functions
gt.set("username")

# returns user's name
gt.name()

# returns user's username
gt.username()

# returns user's bio
gt.bio()

# returns user's total followers
gt.followers()

# returns user's total followings
gt.following()

# returns user's total stars
gt.star()

# returns user's location
gt.location()

# returns user's website
gt.website()

# returns user's twitter
gt.twitter()

# returns user's organization
gt.organization()

# returns user's total projects
gt.count_projects()

# returns user's repositories
gt.count_repositories()
```