import argparse
import codecs
import sys
import yaml

from awesometts import router


def get_services(args):
    for service in router.get_services():
        print('"{:}": {:}'.format(*service))


def get_options(args):
    for option in router.get_options(args.service):
        print(option)


def update_default_options(args):
    user_options = args.options
    for option in router.get_options(args.service):
        if not option.get('key') in user_options.keys() and option.get('default'):
            user_options[option.get('key')] = option.get('default')
    return user_options


def get_mp3(args):
    try:
        if args.text:
            if args.text == "-":
                text = sys.stdin.read()
            else:
                text = args.text
        else:
            with codecs.open(args.file, "r", "utf-8") as f:
                text = f.read()
    except Exception as e:
        print(e)
    name, service = router._fetch_options_and_extras(args.service)
    service['instance'].run(text, update_default_options(args), args.path)


parser = argparse.ArgumentParser()

subparsers = parser.add_subparsers(help='List of commands')

service_parser = subparsers.add_parser('services', help='List of services')
service_parser.set_defaults(func=get_services)

options_parser = subparsers.add_parser('options', help='List of options for service')
options_parser.add_argument('service', help='service name')
options_parser.set_defaults(func=get_options)

tts_parser = subparsers.add_parser('tts', help='Text to mp3')
tts_parser.add_argument('service', help='service name')
tts_parser.add_argument('-d', '--options', type=yaml.load, help='options dict')
tts_parser.add_argument('-t', '--text', nargs='?', help='text to convert')
tts_parser.add_argument('-f', '--file', help='file to convert')
tts_parser.add_argument('-o', '--path', help='path to mp3 file')
tts_parser.set_defaults(func=get_mp3)

args = parser.parse_args()
args.func(args)
