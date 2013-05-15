# imports
import os
import logging
import sys

# module imports
from spotify.manager import (
    SpotifySessionManager, SpotifyPlaylistManager, SpotifyContainerManager)

# logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('session_manager')

logging.basicConfig(level=logging.INFO)
loggerLibSpotify = logging.getLogger('libspotify')

class SessionManager(SpotifySessionManager):

    # the application's developer key
    appkey_file = os.path.join(os.path.dirname(__file__), 'spotify_appkey.key')
    # call when logged in and read
    session_callback = None

    def __init__(self, username=None, password=None):
        SpotifySessionManager.__init__(self, username, password)

    # connect to spotify, does not return until disconnected
    def connect(self):
        logger.info("Connecting")
        super(SessionManager, self).connect()

    # called when logged into spotify
    def logged_in(self, session, error):
        if error:
            logger.error("Error during login:", error)
            return

        logger.info("Logged in as '%s'", session.display_name())
        if self.session_callback:
            self.session_callback(self.session)

    # log messages from libspotify
    def log_message(self, session, message):
        loggerLibSpotify.info(message)

    def connection_error(self, session, error):
        loggerLibSpotify.error('connection_error', error)

    def add_session_callback(self, callback):
        self.session_callback = callback
