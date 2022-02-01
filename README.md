# pygithub-bot

### A Python Bot For Github Automation(Deployed on heroku)


## What the bot does ? :-

- Bot will `greet` to the user whenever he/she create an issue.
- Bot will add label named `review_needed` to the issue whenever it is created.
- Bot will `greet` to the user whenever he/she open a pull request.
- Bot will add label named `review_needed_pr` to the pull request whenever it is being created.
- Bot will react `👍` whenever the comment is created in the issues.(Ok we might not want to actually do that, (and whether it can actually encourage more discussion is questionable). Still, this can be a fun.)


### Repo Stats :-

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-green.svg?style=for-the-badge&color=blue)](.github/CONTRIBUTING.md)
[![GitHub issues](https://img.shields.io/github/issues/vasu-1/PyBot?color=green&logo=github&style=for-the-badge)](https://github.com/vasu-1/PyBot/issues)
[![GitHub PRs](https://img.shields.io/github/issues-pr/vasu-1/PyBot?style=for-the-badge&logo=github)](https://github.com/vasu-1/PyBot/pulls) [![GitHub PRs](https://img.shields.io/github/issues-pr-closed/vasu-1/PyBot?style=for-the-badge&color=critical&logo=github)](https://github.com/vasu-1/PyBot/pulls?q=is%3Apr+is%3Aclosed)


### Language Used :-

![python](https://img.shields.io/badge/python-v3.7-blue?style=for-the-badge&logo=python&logoColor=white)


### Deployment

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/vasu-1/PyBot)

- Create a Heroku project
- Set the `GH_TOKEN` environment variable to the GitHub oauth token to be used by the bot
- Set up the Heroku project to get the code for the bot
- Add `webhook` to the repository in which you want to use the bot
- Set the `GH_SECRET` of webhook in environment variable in heroku
- Deploy on `main` branch and see the `magic` !!
 

### Project Maintainers :-

[![Contributors List](https://contrib.rocks/image?repo=vasu-1/PyBot)](https://github.com/vasu-1/PyBot/graphs/contributors)
