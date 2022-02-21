echo "Running Startup Script"
pm2 stop main_bot
git pull
# For if there have been any changes to the pipefile/dependancies
pipenv install
pm2 start "pipenv run python3 main.py" --name main_bot
