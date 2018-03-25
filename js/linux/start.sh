#!/usr/bin/sh
############################################################################
# Bash script to automate environment configuration for use with node.
# Author: Hayden McParlane
############################################################################

# Verify this script was run with sudo privileges.

# Verify dependencies are installed.
printf "Checking dependencies...\n"
dependencies="$dependencies curl"
for dependency in "${dependencies}"; do
  # Install the dependency if it isn't already present
  if ! [ -x "$(command -v $dependency)" ]; then
    printf "$dependency not found. Installing...\n"
    sudo apt-get install $dependency
  fi

  # Verify that installation was successful.
  if ! [ -x "$(command -v $dependency)" ]; then
    printf "$dependency still not found. Exiting program.\n"
    exit 1
  fi
done

printf "\nFetching and running nvm installer...\n"
if ! [ -x "$(command -v nvm)"]; then
  curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.8/install.sh | bash
fi

# TODO How to modify based on file actually modified by nvm installer.
# TODO How to handle ssh-agents?
if [ "$(command -v nvm)" != "nvm" ]; then
  printf "\nConfiguring environment for nvm use...\n"
  export NVM_DIR="$HOME/.nvm"
  [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
  [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
fi

printf "\nChecking that installation of nvm was successful...\n"
if [ "$(command -v nvm)" != "nvm" ]; then
  printf "\nInstallation of nvm failed. Exiting the program.\n"
  exit 1
fi

# TODO Modify so that user can specify node version
printf "\nInstalling the latest stable node version...\n"
nvm install stable

if ! [ -x "$(command -v node)" ]; then
  printf "\nnode command not recognized. Exiting the program.\n"
  exit 1
fi

printf "\nRunning setup script...\n"
node ../setup.js
