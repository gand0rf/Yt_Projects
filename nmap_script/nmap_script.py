#!/usr/bin/env python3

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
            '\n\t 1: Runs nmap with assume host is alive option and top 100 ports.'
            '\n\t    nmap -Pn  -F [ipaddress]'
            '\n\t 2: Runs nmap with assume host is alive and specific port/ports to scan'
            '\n\t    nmap -Pn -p [port] [ipaddress]'
            '\n\t 3: Runs nmap with OS detection, version detection, script scanning, and traceroute'
            '\n\t    nmap -Pn -A [ipaddress]'
            '\n\t 4: Runs nmap with fragmented packages'
            '\n\t    nmap -Pn -f [ipaddress]'
            '\n\t 5: Runs nmap with a smb enumeration script'
            '\n\t    nmap -Pn --script=smb-enum-shares.nse -p [port] [ipaddress]'
            '\n')
    
def ip_check(ip):
    try:
        ipaddress.ip_address(ip)
        return 1
    except ValueError:
        return 0
    
def port_check(port):
    if len(port) == 1:
        port = port[0].split(',')
        print(port)
    for port_num in port:
        if int(port_num) > 0 and int(port_num) <= 65535:
            continue
        else:
            print('\nInvalid port given\n')
            sys.exit()
    return True


if __name__ == '__main__':
    try:
        if len(sys.argv) < 3:
            print('\nPlease verify your input\n')
            help()
            sys.exit()

        if sys.argv[1] != '-h':

            selection = sys.argv[1]

            if ip_check(sys.argv[2]) == 1:
                ip = sys.argv[2]
            else:
                print('\nInvalid ip address\n')
                help()
                sys.exit()

            if len(sys.argv) > 3 and port_check(sys.argv[3:]) == True:
                port = ''.join(sys.argv[3:])


            match selection:
                case '1':
                    command = subprocess.Popen(['nmap','-Pn','-F',f'{ip}'])
                    command.wait()
                case '2':
                    command = subprocess.Popen(['nmap','-Pn','-p', f'{port}',f'{ip}'])
                    command.wait()
                case '3':
                    command = subprocess.Popen(['nmap','-Pn','-A',f'{ip}'])
                    command.wait()
                case '4':
                    command = subprocess.Popen(['nmap','-Pn','-f',f'{ip}'])
                    command.wait()
                case '5':
                    command = subprocess.Popen(['nmap','-Pn','--script=smb-enum-shares.nse','-p', f'{port}',f'{ip}'])
                    command.wait()
                case _:
                    print('\nNot a valid nmap option\n')
                    help()
        elif sys.argv[1] == '-h':
            help()
    except Exception as error:
        print(f'\nError has occurred:\n\n{error}')
