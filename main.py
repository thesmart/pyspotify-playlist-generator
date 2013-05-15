# imports
from __future__ import unicode_literals
import logging
import os
import sys

# runtime settings, etc
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('main')

# handle environment variables
if __name__ == '__main__':
    environ_kwargs_map = {
        'SPOTIFY_USER': 'username',
        'SPOTIFY_PASS': 'password',
    }

    for environ_key, kwarg in environ_kwargs_map.items():
        if not environ_key in os.environ:
            raise RuntimeError("Missing required environment variable %s" % environ_key)

# script imports
from session_manager import SessionManager

# called when spotify client is connected and ready
def session_callback(session):
    # get all the playlists for this user
    logger.info('session_callback');
    playlist_container = session.playlist_container()
    playlist_container.add_loaded_callback(playlist_container_loaded_callback)

# called when playlist container is finished loading
def playlist_container_loaded_callback(playlist_container, userdata=None):
    logger.info('playlist_container_loaded_callback');



 # connect to Spotify using the SessionManager, and invoke the main function
session_manager = SessionManager(os.environ['SPOTIFY_USER'], os.environ['SPOTIFY_PASS'])
session_manager.add_session_callback(session_callback)
session_manager.connect()

# connect() does not return until disconnected
logger.info('Disconnected.')



