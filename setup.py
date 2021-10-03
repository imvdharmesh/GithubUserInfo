from distutils.core import setup
setup(
  name = 'GithubUserInfo',         # How you named your package folder (MyLib)
  packages = ['GithubUserInfo'],   # Chose the same as "name"
  version = '1.0.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = "Find the user's github account information.",   # Give a short description about your library
  author = 'Dharmesh Vishwakarma',                   # Type in your name
  author_email = 'dharmeshvishwakarma2000@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/imvdharmesh/GithubUserInfo',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/imvdharmesh/GithubUserInfo/archive/refs/tags/pypi-1.0.0.tar.gz',    # I explain this later on
  keywords = ['github', 'githubuserinfo', 'githubuseraccount'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'requests',
          'beautifulsoup4',
      ],
  long_description = 'file:README.md',
  long_description_content_type = 'text/markdown',
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