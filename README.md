# docker-py-update
#!/bin/kerta1n

An extremely simple python script to update Docker compose-d containers
A script I made to update my (and you can too) docker containers. I run debian 11, with the following being how I store files and how this script is intended to work:

`~/docker` holds everything docker container'ed
`~/docker/(container name)` e.g. `~/docker/homeassistant` belongs to each container
`~/docker/(container name)/compose.yml` is the location of the compose file
`~/docker/(container name)/data` is where the container volume is bound to and stores the data

However, if you know a bit of python, feel free to download and edit this script, as its only ~15 lines of python code.
Running the python script is as easy as downloading the raw link with wget or curl (or cloning the repo if you want to waste space) into ~/docker, and then running `python3 update.py`. 
You can also add an alias to make it easy to execute the script. Edit the file `~/.bash_aliases`, and add the line `alias update='python3 ~/docker/update.py'`. After saving and relogging in (!!IMPORTANT!!), you can type update anywhere on your host and update your containers from there. Note that you can also change the `update=` to whatever keyword you want, like `dcu=` (docker compose update). 
