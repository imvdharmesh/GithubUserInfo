from distutils.core import setup
import textwrap
setup(
  name = 'GithubUserInfo',         # How you named your package folder (MyLib)
  packages = ['GithubUserInfo'],   # Chose the same as "name"
  version = '1.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = "Find the user's github account information.",   # Give a short description about your library
  author = 'Dharmesh Vishwakarma',                   # Type in your name
  author_email = 'dharmeshvishwakarma2000@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/imvdharmesh/GithubUserInfo',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/imvdharmesh/GithubUserInfo/archive/refs/tags/pypi-1.0.tar.gz',    # I explain this later on
  keywords = ['github', 'githubuserinfo', 'githubuseraccount'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'requests',
          'beautifulsoup4',
      ],
  long_description =textwrap.dedent(
    """\
    (Tutorial)
    ===========================

    This package is only for Github Public User's Account.

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
      
    /"""
    ),
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)