import sys
import subprocess
import ipaddress


def help():
    print('\nnscript is a tool for running various nmap configs'
            '\n\nFormat: nscript [option] [ip address] [port]'
            '\nPort number is not required. If one is not'
            '\nprovided, port will be set to "-" for all ports'
            '\n\nOptions:'
            '\n\t-h: Prints this help statment.'
            '\n\t 1: Runs namp with no options.'
            '\n\t    nmap [ipaddress]'
            '\n\t 2: Runs nmap with the top 100 ports option.'
            '\n\t    nmap -F [ipaddress]'
            '\n\t 3: Runs nmap with assume host is alive option.'
            '\n\t    nmap -Pn [ipaddress]'
            '\n\t 4: Runs nmap with assume host is alive option and top 100 ports.'
            '\n\t    nmap -Pn  -F [ipaddress]'
            '\n\t 5: Runs nmap with scan on traget port only.'
            '\n\t    nmap -p [port] [ipaddress]'
            '\n')
    
def ip_check(ip):
    try:
        ipaddress.ip_address(ip)
        return 1
    except ValueError:
        return 0

try:
    if sys.argv[1] != '-h':

        selection = sys.argv[1]

        if ip_check(sys.argv[2]) == 1:
            ip = sys.argv[2]
        else:
            print('\nInvalid ip address\n')
            help()
            sys.exit()

        if sys.argv[3] != '' and int(sys.argv[3]) <= 65535 and int(sys.argv[3]) > 0:
            port = sys.argv[3]
        elif int(sys.argv[3]) > 65535 or int(sys.argv[3]) < 0:
            print('\nInvalid port number\n')
            help()
            sys.exit()
        else:
            port = '-'

        match selection:
            case '1':
                command = subprocess.Popen(['nmap',f'{selection}',f'{ip}'])
                command.wait()
            case '2':
                command = subprocess.Popen(['nmap','-F',f'{selection}',f'{ip}'])
                command.wait()
            case '3':
                command = subprocess.Popen(['nmap','-Pn',f'{selection}',f'{ip}'])
                command.wait()
            case '4':
                command = subprocess.Popen(['nmap','-Pn','-F',f'{selection}',f'{ip}'])
                command.wait()
            case '5':
                command = subprocess.Popen(['nmap','-p', f'{port}',f'{selection}',f'{ip}'])
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