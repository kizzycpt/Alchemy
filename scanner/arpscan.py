#imports
from scapy.all import ARP, Ether, sendp, srp
from rich console.import.console

#color change variable
Console() = console


"""def arp_scan():

    arp=ARP(pdst=subnet)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")

    try:
        result
    except PermissionError:
        console.print("[red][!] Scapy needs raw-socket permission for ARP on Linux.[/red]")
        console.print("[yellow]Run with sudo, or grant CAP_NET_RAW/CAP_NET_ADMIN to the interpreter.[/yellow]")
        return {}

    hosts: dict[str, str] = {}
    for _, received in result:
        if not quiet:
            print(f"[+] Host found: {received.psrc} - MAC: {received.hwsrc}")
        hosts[received.psrc] = received.hwsrc
    return hosts

    """
