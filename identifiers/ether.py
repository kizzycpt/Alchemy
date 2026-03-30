from scapy.all import *
import ipaddress, socket, time
from rich.console import Console
from rich.table import Table
from rich.live import Live
import time
import socket
from termcolor import colored
import netifaces
import ipaddress
from .gateway import gateway_info


#Unwanted Interface Prefixes

bad_iface_prefixes = ("lo", "docker", "wg", "br-", "veth", "virbr", "zt", "vboxnet")

#----------------------------------------------------------------------------------------------

#Subnet Information
def get_subnet():
    try:
        local_ip = socket.gethostbyname(socket.gethostname())
        subnet_mask = "255.255.255.0"
        network = ipaddress.IPv4Network(f"{local_ip}/{subnet_mask}", strict = False)
        cidr = str(network.network_address) + "/24"

        return cidr
    except Exception as e:
        print(f"error. {e}")
        return None


#----------------------------------------------------------------------------------------------

# Grabbing target IP based off input
def get_mac(ip):
   
   #MAC variables 
    arp_req = ARP(pdst = ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
   
    #ARP Packet Formula
    arp_packet = broadcast/arp_req

    #Reply loop for ARP Request
    answered, _ = srp(arp_packet, timeout = 2, verbose = 0)
    for sent, received in answered:
        return received.hwsrc
    
    return None

#Recieving Source MAC for Packet Sending
def get_my_mac():
    try:
        for iface in netifaces.interfaces():
            if iface.startswith(bad_iface_prefixes):
                continue
            
            addrs = netifaces.ifaddresses(iface)
            iface_link = addrs.get(netifaces.AF_LINK)
            
            if not iface_link:
                continue

            my_mac = iface_link[0].get("addr")
            if my_mac and my_mac != "00:00:00:00:00:00":
                return {"Interface": iface, "MAC": my_mac}
        return None


    except Exception as e:
        print(f"Error in resolving MAC Address. {e}.")
        return {}


#ARP Broadcast: Replies with IP:MAC
def arp_scan(quiet: bool = False ) -> dict[str, str]:
    
    subnet = get_subnet()

    arp = ARP(pdst=subnet)
    ether = Ether(dst = "ff:ff:ff:ff:ff:ff")

    packet = ether/arp

    try:
        result, _ = srp(packet, timeout = 0, verbose = 0)
    except PermissionError:
        console.print = ("[red] Scapy needs permission for ARP scan on linux. [/red]]")
        return {}
    
    hosts: dict[str, str] = {}
    for sent, received in result:
        if not quiet:
            print(f"hosts found: {received.psrc} - MAC: {received.hwsrc}\n")
        hosts[received.psrc] = received.hwsrc
    return hosts