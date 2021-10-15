"""
This port scanner is a tutorial follow along built from the ZTM ethical hacking course.
"""

import socket
import termcolor


def scan(target, ports):
    print('\n' + 'Starting scan for ' + str(target))
    for port in range(1, ports):
        scan_port(target, port)


def scan_port(ipaddress, port):
    """
    :param ipaddress: User's Ip address
    :param port: The port that is scanned
    :return: Port number or port closed, with message.
    """
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print("[+] Port Opened " + str(port))
        sock.Close()
    except:
        pass


targets = input("[*] Enter targets to scan (Split them with ,): ")
ports = int(input("[*] Enter how many ports you wish to scan: "))
if ',' in targets:
    print(termcolor.colored("[*] Scanning multiple targets", 'red'))
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '), ports)
else:
    scan(targets, ports)
