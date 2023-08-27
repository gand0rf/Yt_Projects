import sys
import subprocess


def help():
    print('\nnscript is a tool for running various nmap configs'
            '\n\nFormat: nscript [option] [ip address]'
            '\n\nOptions:'
            '\n\t-h: Prints this help statment.'
            '\n\t 1: Runs namp with no options.'
            '\n\t    nmap [ipaddress]'
            '\n\t 2: Runs nmap with the fast option.'
            '\n\t    nmap -F [ipaddress]'
            '\n')

try:
    if sys.argv[1] != '-h':
        selection = sys.argv[1]
        ip = sys.argv[2]
        match selection:
            case '1':
                command = subprocess.Popen(['nmap',f'{selection}',f'{ip}'])
                command.wait()
            case '2':
                command = subprocess.Popen(['nmap','-F',f'{selection}',f'{ip}'])
                command.wait()
            case _:
                print('\nNot a valid nmap option\n')
                help()
    elif sys.argv[1] == '-h':
        help()
except IndexError:
    print('\nPlease enter valid option and ip address for program\n')
    help()
except Exception as error:
    print(f'\nError has occurred:\n\n{error}')