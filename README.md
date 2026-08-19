# Alchemy

> **⚠️ Legacy / archived.** This is a V1 educational MITM toolkit and is no longer actively developed. It is kept as a reference snapshot. Do not expect maintenance.

A Python + Scapy tool for Layer-2 network reconnaissance and ARP-based MITM demonstrations, with a Rich/PyFiglet CLI.

> **Authorized use only.** This performs ARP cache poisoning, an active MITM attack. Run it **only** on networks you own or are explicitly authorized to test. The author is not responsible for misuse.

---

## What it does

- Auto-detects the local subnet
- ARP-scans the LAN to discover hosts (IP ⇄ MAC)
- Resolves your own interface/MAC and a target's MAC
- Reads gateway information
- Crafts and sends ARP cache-poisoning packets:
  - **Classic** cache poison (target ↔ gateway)
  - **VLAN** (802.1Q double-tag) variant
- Styled CLI via [Rich](https://github.com/Textualize/rich) and [PyFiglet](https://github.com/pwaller/pyfiglet)

---

## Layout

```
alchemy/
├─ alchemy.py                # entrypoint (menu)
├─ identifiers/
│  ├─ ether.py               # subnet, MAC resolution, ARP scan
│  └─ gateway.py             # gateway IP/MAC lookup
└─ poisons/
   └─ ARP.py                 # classic + VLAN ARP cache poisoning
```

---

## Requirements

- Python 3.10+
- Linux (raw sockets for Scapy)
- Root / `CAP_NET_RAW` for sending crafted frames

Packages: `scapy`, `rich`, `pyfiglet`, `termcolor`, `netifaces` — see `requirements.txt`.

---

## Install & run

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

sudo -E python3 alchemy.py
```

Menu: `1` ARP poison (then choose classic or VLAN) · `2` exit.

Run inside a virtual environment, and only against authorized targets.

---

## Status

V1 — Layer-2 MITM and sniffing. Archived; superseded by later tooling.
