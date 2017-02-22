# -*- coding: utf-8 -*-

# AwesomeTTS text-to-speech add-on for Anki
# Copyright (C) 2010-Present  Anki AwesomeTTS Development Team
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Add-on package initialization
"""

from os.path import join
from time import time


from . import conversion as to, paths, service
from .bundle import Bundle
from .config import Config

from .router import Router


__all__ = ['browser_menus', 'cards_button', 'config_menu', 'editor_button',
           'reviewer_hooks', 'sound_tag_delays', 'update_checker',
           'window_shortcuts']


def get_platform_info():
    """Exception-tolerant platform information for use with AGENT."""

    implementation = system_description = "???"
    python_version = "?.?.?"

    try:
        import platform
    except:  # catch-all, pylint:disable=bare-except
        pass
    else:
        try:
            implementation = platform.python_implementation()
        except:  # catch-all, pylint:disable=bare-except
            pass

        try:
            python_version = platform.python_version()
        except:  # catch-all, pylint:disable=bare-except
            pass

        try:
            system_description = platform.platform().replace('-', ' ')
        except:  # catch-all, pylint:disable=bare-except
            pass

    return "%s %s; %s" % (implementation, python_version, system_description)

VERSION = '1.11.0-dev'

WEB = 'https://ankiatts.appspot.com'

AGENT = 'AwesomeTTS/1.10.0 (Anki 2.0.33; PyQt 4.11.4; %s)' % get_platform_info()


# Begin core class initialization and dependency setup, pylint:disable=C0103

logger = Bundle(debug=lambda *a, **k: None, error=lambda *a, **k: None,
                info=lambda *a, **k: None, warn=lambda *a, **k: None)
# for logging output, replace `logger` with a real one, e.g.:
# import logging as logger
# logger.basicConfig(stream=sys.stdout, level=logger.DEBUG)

router = Router(
    services=Bundle(
        mappings=[
            ('abair', service.Abair),
            ('baidu', service.Baidu),
            ('collins', service.Collins),
            ('duden', service.Duden),
            ('ekho', service.Ekho),
            ('espeak', service.ESpeak),
            ('festival', service.Festival),
            ('fluencynl', service.FluencyNl),
            ('google', service.Google),
            ('howjsay', service.Howjsay),
            ('imtranslator', service.ImTranslator),
            ('ispeech', service.ISpeech),
            ('naver', service.Naver),
            ('neospeech', service.NeoSpeech),
            ('oddcast', service.Oddcast),
            ('oxford', service.Oxford),
            ('pico2wave', service.Pico2Wave),
            ('rhvoice', service.RHVoice),
            ('sapi5js', service.SAPI5JS),
            ('say', service.Say),
            ('spanishdict', service.SpanishDict),
            ('voicetext', service.VoiceText),
            ('wiktionary', service.Wiktionary),
            ('yandex', service.Yandex),
            ('youdao', service.Youdao),
        ],
        dead=dict(
            ttsapicom="TTS-API.com has gone offline and can no longer be "
                      "used. Please switch to another service with English.",
        ),
        aliases=[('b', 'baidu'), ('g', 'google'), ('macosx', 'say'),
                 ('microsoft', 'sapi5js'), ('microsoftjs', 'sapi5js'),
                 ('microsoftjscript', 'sapi5js'), ('oed', 'oxford'),
                 ('osx', 'say'), ('sapi', 'sapi5js'), ('sapi5', 'sapi5js'),
                 ('sapi5jscript', 'sapi5js'), ('sapijs', 'sapi5js'),
                 ('sapijscript', 'sapi5js'), ('svox', 'pico2wave'),
                 ('svoxpico', 'pico2wave'), ('ttsapi', 'ttsapicom'),
                 ('windows', 'sapi5js'), ('windowsjs', 'sapi5js'),
                 ('windowsjscript', 'sapi5js'), ('y', 'yandex')],
        normalize=to.normalized_ascii,
        args=(),
        kwargs=dict(temp_dir=paths.TEMP,
                    lame_flags=lambda: config['lame_flags'],
                    normalize=to.normalized_ascii,
                    logger=logger,
                    ecosystem=Bundle(web=WEB, agent=AGENT)),
    ),
    cache_dir=paths.CACHE,
    temp_dir=join(paths.TEMP, '_awesometts_scratch_' + str(int(time()))),
    logger=logger,
    config=config,
)
