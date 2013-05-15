# Playlist Generator for PySpotify

This is a playlist generator script of PySpotify and libspotify.  It currently doesn't work, and serves as an example for a fix from the industry and community.

## General Requirements

You must have a Spotify Premium account and an application key:
https://developer.spotify.com/technologies/libspotify/

You'll need to install python 2.7.3, pip, pyspotify, and libspotify.

## Contents

### logs.txt

logs from operation demonstrating libspotify errors

### spotify_appkey.key

Make sure you have an application key saved to ```spotify_appkey.key``` in the project root.

### main.py

The main script to execute.

## Setup

This all works on OSX, but the brew steps can be substituted with apt-get.

    Install Brew

    ```
    sudo ruby -e "$(curl -fsSL https://raw.github.com/mxcl/homebrew/go)"
    sudo brew update
    sudo brew upgrade
    ```

    Install libspotify

    ```
    sudo brew install libspotify
    ```

    Install python 2.7. (usually installed by default):

    ```
    $ python --version
    Python 2.7.1
    ```

    Install pip and virtualenv:

    ```
    sudo easy_install pip
    sudo pip install virtualenvwrapper
    ```

    You then append to your .bash_login file:

    ```
    export WORKON_HOME
    source /usr/local/bin/virtualenvwrapper.sh

    export SPOTIFY_USER='any_spotify_username'
    export SPOTIFY_PASS='any_spotify_password'
    ```

    Source your .bash_login:

    ```
    source ~/.bash_login
    ```

    Create an environment for the python script, then swap to that environment:

    ```
    git clone git@github.com:thesmart/pyspotify-playlist-generator.git
    cd pyspotify-playlist-generator
    mkvirtualenv env-pyspotify-playlist-generator
    source env-pyspotify-playlist-generator/bin/activate
    ```

    Install the necessary python modules:

    ```
    pip install pyspotify==1.10
    ```

    Now run that puppy.

    ```
    python main.py
    ```

### Issues:

libspotify throws ChannelError. See ```logs.txt```.