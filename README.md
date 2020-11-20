# telegram_heroku

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
