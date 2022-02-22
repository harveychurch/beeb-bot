# Beeb Bot
> A Bot for the Private BBC Apprentice & Trainee Discord

## What is this?

This is designed to allow any BBC Trainee & Apprentice (*or any other who wishes*) to add functionality, test out programming skills or just for fun!

The functionality is such that each `command` can be its own file and then is loaded.

### Requirements

This project uses:
* Python 3.8+
* discord.py
* [Pipenv](https://pypi.org/project/pipenv/) for package management

## How to run the Project?

### Local Development

Clone this project and then:

1. Run `pipenv install` to install the currently listed modules.
2. Go to https://discord.com/developers/applications and create an application
3. After creating, the appliication. Proceed to the `Bot` page, `Add Bot` and copy the generated token.
4. Make a copy of the `.env(template)`, re-name it to `.env` and paste your generated token where `????` currently is
5. Run `main.py` and your application should log in and be assessible. 
**NOTE: You will need to add the bot to a server to interact with it**

### Server Deployment

#### **This Project**

To trigger a release, a git tag is created. The format for this is the [`MAJOR.MINOR.PATCH`](https://semver.org/) format.

The GitHub action triggers two functions:
* [Creates a Release](https://github.com/harveychurch/beeb-bot/releases)
* Triggers the Deployment to the remote server.
  * The servers uses PM2 to create a daemon which is stopped and started between a `git pull` and a `pipenv install` (incase of a change in Python modules)

#### **Cloned Project**
This project makes usage of GitHub actions to automate the deployment. 

You can duplicate this functionality by adding the following as GitHub secrets on your cloned repo (in brackets is the name of the SECRET):

* Host IP of remote server (HOST)
* Private SSH Key associated with Public-Private Key pair (SSHKEY)
* Password *optional* (PASSWORD)
* Username for Remote Server (USER)

**Note:** The name that each secret is stored under is _important_ as they are directly reference in the `.github/workflows` YAML file.

---

## Contributing

Contribute away! 

1. **Fork** the repo on GitHub
 2. **Clone** the project to your own machine
 3. **Commit** changes to your own branch
 4. **Push** your work back up to your fork
 5. Submit a **Pull request** so that we can review your changes

NOTE: Be sure to merge the latest from "upstream" before making a pull request!

Most code should be submitted in your own ["Cog"](https://discordpy.readthedocs.io/en/stable/ext/commands/cogs.html). Refer to the `modules/test_cog.py` for the basic example.

### Basic Cog Format

Each cog must contain a:
* Setup method
* Class that extends `command.Cogs`


## License 

This project is licensed under MIT. See `LICENSE` for the full text.