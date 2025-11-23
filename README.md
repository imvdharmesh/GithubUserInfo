# 📦 GithubUserInfo
A simple Python package to fetch **public GitHub user profile details** using web scraping.

This package allows developers to quickly retrieve information about any public GitHub profile such as username, full name, bio, followers, stars, repositories, and more.

---

## 🚀 Installation

Install using **pip**:

```bash
pip install GithubUserInfo

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
