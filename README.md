# mycroft-skill-simple-media-controls
This is a 3rd party skill that adds simple media controls, play, pause, prev, next mapped to shell commands.  This will allow you to use whatever program you like as long as you can write a script.

If you're looking for a good mpg123/spotify/mopidy mycroft skill try this one https://github.com/forslund/mycroft-media-skills

I prefer to to use [fmp](https://github.com/the7erm/fmp-pg) and just wanted to write a dumb wrapper to run a script that did most of the heavy lifting.

The commands are simple.

    mycroft play

    During testing mycroft misunderstood the word pause a lot.
    mycroft pause
            paws
            posh
            pawn
            polish
            boss
            cars

    mycroft next

    mycroft previous

    mycroft what's playing?
            what is playing?
            what am I listening to?
            what is this song?
            what is this file?
            who is this?
            what band is this?

# Configuring `mycroft.conf`
```json
{
    "SimpleMediaSkill": {
        "play": "/home/erm/bin/play.sh",
        "pause": "/home/erm/bin/pause.sh",
        "next": "/home/erm/bin/next.sh",
        "prev": "/home/erm/bin/prev.sh",
        "whats_playing": "/home/erm/bin/playing.sh"
    }
}
```

# Install

```
cd /opt/mycroft/skills
git clone https://github.com/the7erm/mycroft-skill-diagnostics.git skill-simpile-media-controls
cd skill-simpile-media-controls
workon mycroft
# if that doesn't work try `source <path to virtualenv/bin/activate>`
pip install -r requirements.txt
# restart the skills service
```

# Sample scripts
I've written a couple of scripts to get you started.  Keep in mind these might not work if the screen saver is on.

- [`samples/fmp`](https://github.com/the7erm/mycroft-skill-simple-media-controls/tree/master/samples/fmp) - [fmp](https://github.com/the7erm/fmp-pg)
- [`samples/xdotool`](https://github.com/the7erm/mycroft-skill-simple-media-controls/tree/master/samples/xdotool) - [xdotool](https://www.semicomplete.com/projects/xdotool/xdotool.xhtml) - emulates `XF86AudioPlay`, `XF86AudioPrev`, and `XF86AudioNext` being pressed.

If you write your owns scripts, please feel free to fork the project, add them to the `samples/` and create a pull request.
