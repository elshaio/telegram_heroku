# telegram_heroku

Simple Bot for send messages to your telegram using an api that wraps your token inside heroku.
I use it just to know my chat_id when I forget it usin `/getchatid` or to send messages of my sh scripts using a curl.

## Creating a bot
First you must want to create a bot and get your token for send messages, please call to [BotFather](https://telegram.me/BotFather) and then you have a token, save it for later.

## Creating a heroku account
Then you need to create a heroku account to deploy the script, go to [heroku](https://id.heroku.com/login), create an account and install the cli, for the las thing you can follow this [instructions](https://devcenter.heroku.com/articles/heroku-cli).

## Installing the script on heroku
Finally, just follow the next instructions, they will create a new app, enable metadata that the script automatically will know your app name, and set token and other stuff that puts the app running. Remember:

| Variable      | Description                                                                                               |
| ---           | ---                                                                                                       |
| appname       | your personal app name, remember you future url will be something like `https://<appname>.herokuapp.com/` |
| telegramtoken | The token that you receive from `BotFather`                                                               |

### Script instructions

```bash
# Create a heroku app.
heroku apps:create <appname>

# Enable labs to tell main what is the appname through env variables.
heroku labs:enable runtime-dyno-metadata -a <appname>

# Add to the current repository the "heroku" remote to push the app.
heroku git:remote -a <appname>

# Set TOKEN env for telegram
heroku config:set -a <appname> TOKEN=<telegramtoken>

# Finally, push
git push heroku master
```
