# Alchemy Poisons

**Disclaimer**  
This project demonstrates scanning and poisoning (MITM) techniques using Python and Scapy.
Currently V1 (Layer 2 MITM and Sniffing)  
It is provided **strictly for educational and research purposes only**.  
Do not use it on networks without **explicit authorization**.  
The author is not responsible for any misuse of this tool.

---

##  Features
- Detects local network subnet automatically.
- Performs ARP scans to discover devices (IP, MAC, Hostname).
- Demonstrates ARP packet crafting for educational purposes.
- CLI interface with styled output using [Rich](https://github.com/Textualize/rich) and [PyFiglet](https://github.com/pwaller/pyfiglet).

---

##  Requirements
See [requirements.txt](requirements.txt) for the full list.  
Key dependencies:
- scapy  
- rich  
- pyfiglet  
- termcolor  
- netifaces  

Install with:

```bash

pip install -r requirements.txt

**Be sure to run this script under a contained/virtual environment.** 
