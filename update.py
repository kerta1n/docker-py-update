import os
import sys
def update():
  print("Welcome to the Docker update script! Type the directory name of the container that you want to update, exactly as it shows. (Run ls in this directory if you're not sure and hit control and c at any time to stop this script.)")
  target = input()
# if target in ["all"]:
# else: 
#   pass
  os.system("docker compose -f " + target + "/docker-compose.yml up -d --force-recreate")
  print("Would you like to exit, or restart the script? Type your choice exactly as written. ")
  done = input()
  if done in ["restart"]:
    update()
  elif done in ["exit"]:
    sys.exit("run 'python3 update.py' to update another container, bye for now")
update()