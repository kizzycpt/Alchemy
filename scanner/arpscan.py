#imports
from scapy.all import ARP, Ether, sendp, srp
from rich console.import.console

#color change variable
Console() = console


def arp_scan():
    arp =ARP(pdst=subnet)
    