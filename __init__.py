# Copyright 2016 Eugene R. Miller
#
# This file is a 3rd party skill for mycroft.
#
# The Mycroft Simple Media Controls skill is free software: you can
# redistribute it and/or modify it under the terms of the GNU
# General Public License as published by the Free Software Foundation, either
#  version 2 of the License, or (at your option) any later version.
#
# diagnostics kill is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with the diagnostics skill.  If not, see <http://www.gnu.org/licenses/>.

from os.path import dirname, exists, isfile
from os import access, X_OK
import sys

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
import subprocess
import json

__author__ = 'the7erm'

LOGGER = getLogger(__name__)

def is_exe(fpath):
    # Attribution: http://stackoverflow.com/a/377028/2444609
    return isfile(fpath) and access(fpath, X_OK)


class SimpleMediaSkill(MycroftSkill):

    def __init__(self):
        super(SimpleMediaSkill, self).__init__(name="SimpleMediaSkill")

    def initialize(self):
        self.load_data_files(dirname(__file__))

        play_intent = IntentBuilder("PlayMediaIntent")\
            .require("PlayMediaKeyword")\
            .build()
        self.register_intent(play_intent, self.handle_play_intent)

        pause_intent = IntentBuilder("PauseMediaIntent")\
            .require("PauseMediaKeyword")\
            .build()
        self.register_intent(pause_intent, self.handle_pause_intent)

        next_intent = IntentBuilder("NextMediaIntent")\
            .require("NextMediaKeyword")\
            .build()
        self.register_intent(next_intent, self.handle_next_intent)

        prev_intent = IntentBuilder("PrevMediaIntent")\
            .require("PreviousMediaKeyword")\
            .build()
        self.register_intent(prev_intent, self.handle_prev_intent)

        whats_playing_intent = IntentBuilder("WhatsPlayingMediaIntent")\
            .require("WhatsPlayingMediaKeyword")\
            .build()
        self.register_intent(whats_playing_intent,
                             self.handle_whats_playing_intent)

    def run_cmd(self, cmd):
        if self.config is None:
            self.speak_dialog("missing.config")
            return

        exe_cmd = self.config.get(cmd)
        spec = {
            "filename": cmd
        }

        if exe_cmd is None:
            self.speak_dialog("missing.config.command", spec)
            return
        try:
            return subprocess.check_output([exe_cmd])
        except:
            e = sys.exc_info()[0]
            LOGGER.error("error:%s" % e)
            if "/" in cmd:
                if not exists(cmd):
                    self.speak_dialog("missing", spec)
                elif not is_exe(cmd):
                    self.speak_dialog("cant.run", spec)
                else:
                    self.speak_dialog("error.executing", spec)
            else:
                self.speak_dialog("error.executing", spec)


    def handle_play_intent(self, message):
        LOGGER.debug("handle_play_intent")
        self.run_cmd("play")

    def handle_pause_intent(self, message):
        LOGGER.debug("handle_pause_intent")
        self.run_cmd("pause")

    def handle_next_intent(self, message):
        LOGGER.debug("handle_next_intent")
        self.run_cmd("next")

    def handle_prev_intent(self, message):
        LOGGER.debug("handle_prev_intent")
        self.run_cmd("prev")

    def handle_whats_playing_intent(self, message):
        LOGGER.debug("handle_whats_playing")
        res = self.run_cmd("whats_playing")
        if res:
            spec = {
                "playing": res
            }
            self.speak_dialog("whats_playing", spec)


    def stop(self):
        pass


def create_skill():
    return SimpleMediaSkill()
