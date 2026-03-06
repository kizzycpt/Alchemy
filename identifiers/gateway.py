import netifaces
import ipaddress
import requests
import subprocess



def gateway_info():
    #Gateway Variables
    gws = netifaces.gateways()
    router_ip, iface = gws["default"][netifaces.AF_INET]
    ip_info = netifaces.ifaddresses(iface)[netifaces.AF_INET][0]
    addr  = ip_info["addr"]
    mask = ip_info["netmask"]
    subnet = ipaddress.IPv4Network(f"{addr}/{mask}", strict = False)
    
    try:
        info = {"Gateway": router_ip,"Interface": iface, "Subnet": subnet}

    except Exception as e:
        print(f"[!]Error! {e}. Please try again. [!]")
        return None
