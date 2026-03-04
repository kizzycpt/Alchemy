import netifaces
import ipaddress
import requests
import sys
import subprocess

def gateway_info():
    try:
        gws = netifaces.gateways()
        router_ip, iface = gws["default"][netifaces.AF_INET]
        ip_info = netifaces.ifaddresses(iface)[netifaces.AF_INET][0]

        info = {"Gateway": router_ip,"Interface": iface, "MAC": router_mac}
        
        

    except Exception as e:
        print(f"[!]Error! {e}. Please try again. [!]")
        return None
