from argui.backends.tk import ArgumentDialogTk as ArgumentDialog
from argui.backends.tk import show_dialog_tk as show_dialog

import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

'''
1. GUI
2. Command Line
3. Environment Variables
4. Local Configuration File
5. Home Configuration File
6. System Configuration File
7. Script's Defaults
'''


def parse_args_gui(parser, argv=None):
    argv = sys.argv if argv is None else argv
    return show_dialog_tk(parser, argv)

args = parse_args_gui(parser,)
args = parser.parse_args()
print(args.accumulate(args.integers))
