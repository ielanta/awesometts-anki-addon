# AwesomeTTS Anki add-on

AwesomeTTS makes it easy for language-learners and other students to add
speech to their personal [Anki](https://apps.ankiweb.net) card decks.

Once loaded into the Anki `addons` directory, the AwesomeTTS add-on code
enables both on-demand playback and recording functionality.

# How to use
#### Get list of services
```
manage.py services [-h]
```

#### Get list of options
```
manage.py options [-h] service
```
positional arguments:
  - service     service name

#### Text to mp3
```
manage.py tts [-h] [-d OPTIONS] [-t [TEXT]] [-f FILE] [-o PATH] service
```

positional arguments:
  - service:               service name

optional arguments:
  - -h, --help:            show this help message and exit
  - -d OPTIONS, --options OPTIONS: options dict
  - -t [TEXT], --text [TEXT]: text to convert
  - -f FILE, --file FILE:  file to convert
  - -o PATH, --path PATH:  path to mp3 file


## License

AwesomeTTS is free and open-source software. The add-on code that runs within
Anki is released under the [GNU GPL v3](LICENSE.txt).
