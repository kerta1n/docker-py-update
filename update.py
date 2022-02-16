import os
import sys
def update():
  print("Welcome to the Docker update script! This script updates system packages in order to ensure proper container updates. Press enter to update system packages. Press control and c to stop.")
  i = input()
  print("Updating host OS packages, please enter sudo password if needed...")
  os.system("sudo apt update")
  os.system("sudo apt upgrade")
  print("Purging and autoremoving unused packages to free up disk space...")
  os.system("sudo apt remove --purge --autoremove") 
  print("Type the directory name of the container that you want to update, exactly as it shows. (Run ls in this directory if you're not sure and hit control and c at any time to stop this script.)")
  target = input()
  os.system("cd ~/docker/" + target)
  os.system("docker compose down --rmi all")
  os.system("docker compose up -d --force-recreate")
  os.system("cd")
  print("Would you like to exit, or restart the script? Type your choice exactly as written. Leave blank and hit enter to cancel. ")
  done = input()
  if done in ["restart"]:
    update()
  elif done in ["exit"]:
    print("Run 'python3 update.py' to update another container, bye for now")
    sys.exit
update()
