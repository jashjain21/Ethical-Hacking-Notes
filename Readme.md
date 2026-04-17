# 🔐 Ethical Hacking Notes — Practical Penetration Testing Study Guide

## 🚀 Overview

A structured collection of hands-on ethical hacking and penetration testing notes covering 18 modules — from networking fundamentals and Linux basics through Active Directory attacks, buffer overflow exploitation, OWASP Top 10 web vulnerabilities, and post-exploitation techniques. Includes step-by-step walkthroughs of 20+ HackTheBox machines with annotated screenshots, plus a Python port scanner and a full Kioptrix assessment with findings documentation.

These notes were taken while working through a practical ethical hacking course, with each topic organized into numbered subtopics containing HTML notes and annotated screenshots from live lab environments.

## 📚 Modules

| # | Module | Topics Covered |
|---|---|---|
| 1 | **Networking Refresher** | IP addresses, MAC addresses, TCP/UDP, OSI model, subnetting, common ports/protocols |
| 2 | **Intro to Linux** | File system navigation, file operations, users & privileges, services, bash scripting |
| 3 | **Intro to Python** | Sockets, strings, port scanner script |
| 4 | **Information Gathering** | Passive recon, Google dorking, subdomain hunting, theHarvester, Burp Suite, social media OSINT, breach credential gathering |
| 5 | **Scanning & Enumeration** | Nmap scanning, Kioptrix setup, HTTP/HTTPS enumeration, SMB enumeration, SSH enumeration, vulnerability research |
| 6 | **Assessment Notes** | Full Kioptrix assessment — nmap results, findings, exploitation (SMB trans2open), post-exploitation |
| 7 | **Additional Scanning Tools** | Nessus, Metasploit scanner, Masscan |
| 8 | **Exploitation Basics** | Reverse vs. bind shells, staged vs. non-staged payloads, Metasploit exploitation, brute force attacks, password spraying, credential stuffing |
| 9 | **Mid-Course Capstone** | 20+ HackTheBox machine walkthroughs (Legacy, Lame, Blue, Devel, Jerry, Nibbles, Optimum, Bashed, Grandpa, Granny, Netmon, Bastard, Shocker, Valentine, Sunday, Bounty, and more) |
| 10 | **Intro to Exploit Development** | Buffer overflow explained, spiking, fuzzing, finding offsets, overwriting EIP, bad characters, finding the right module, gaining root |
| 11 | **Active Directory Overview** | AD concepts, physical components (domain controllers, AD DS data store), logical components (domains, trees, forests, OUs, trusts, objects) |
| 12 | **Active Directory Lab Build** | Setting up domain controller, user machines, users/groups/policies, joining machines to domain |
| 13 | **Attacking AD — Initial Vectors** | LLMNR poisoning, NTLMv2 hash capture with Responder, hashcat cracking, SMB relay attacks, SMB signing discovery, shell access, IPv6 DNS takeover via mitm6, LDAPS setup |
| 14 | **Attacking AD — Post Compromise** | PowerView overview, BloodHound setup, data collection with Invoke-BloodHound |
| 15 | **Attacking AD — Post Compromise (Advanced)** | Pass the hash/password, secretsdump.py, NTLM hash cracking, token impersonation with Incognito, Kerberoasting, GPP/cPassword attacks, Mimikatz, Golden Ticket attacks |
| 16 | **Post Exploitation** | File transfers, maintaining access, pivoting (lab setup + walkthrough), cleaning up |
| 17 | **Web App Enumeration Revisited** | Go installation, Assetfinder, Amass, httprobe, GoWitness screenshots, automated enumeration |
| 18 | **OWASP Top 10 Web Vulnerabilities** | Juice Shop setup, Burp Suite, FoxyProxy, SQL injection (attacks + walkthrough + defenses), broken authentication, sensitive data exposure, XXE, broken access control, security misconfigs, XSS |

## 🛠 Tools Covered

Nmap, Metasploit, Nessus, Masscan, Burp Suite, Responder, hashcat, Mimikatz, BloodHound, PowerView, Incognito, secretsdump.py, mitm6, theHarvester, Assetfinder, Amass, httprobe, GoWitness, FoxyProxy, OWASP Juice Shop

## 💻 Code

- **`scanner.py`** — Python port scanner using sockets with hostname resolution, timeout handling, and keyboard interrupt support
- **`3.Intro_to_python/`** — Socket programming examples and string manipulation notes

## 🏗 Structure

Notes are organized as a notebook export with each module containing numbered subtopics. Each subtopic has:
- `page.html` — The note content with embedded text and image references
- `image*.png` — Annotated screenshots from lab environments
- `node.xml` — Notebook metadata

```
Ethical-Hacking-Notes/
├── 1.networking refresher/       # OSI, TCP/UDP, subnetting
├── 2.Intro_to_linux/             # Linux fundamentals
├── 3.Intro_to_python/            # Sockets, port scanner
├── 4.Information_Gathering/      # OSINT, recon tools
├── 5.Scanning_enumeration/       # Nmap, SMB, HTTP enum
├── 6.Assessment Notes/           # Kioptrix full assessment
├── 7.Additional Scanning Tools/  # Nessus, Masscan
├── 8.Exploitation_Basics/        # Shells, Metasploit, brute force
├── 9.Mid-Course-Capstone/        # 20+ HackTheBox walkthroughs
├── 10.Intro_to_exploit_development/  # Buffer overflow
├── 11.Active Directory Overview/     # AD concepts
├── 12.Active Directory Lab Build/    # Lab setup
├── 13.Attacking AD Initial Attack Vectors/  # LLMNR, SMB relay
├── 14.Attacking AD-Post Compromise/  # BloodHound, PowerView
├── 15.Attacking Ad-Post Compromise/  # Kerberoasting, Mimikatz
├── 16.Post Exploitation/             # Pivoting, persistence
├── 17.Web Application Enumeration Revisited/  # Subdomain tools
└── 18.Testing Top 10 Web App Vulnerabilities/ # OWASP Top 10
```

## 🔍 What This Covers

- **Network Penetration Testing** — From reconnaissance through exploitation to post-exploitation and cleanup
- **Active Directory Attacks** — Full attack chain: LLMNR poisoning → hash cracking → pass the hash → token impersonation → Kerberoasting → Golden Ticket
- **Web Application Security** — OWASP Top 10 with hands-on Juice Shop walkthroughs
- **Buffer Overflow Exploitation** — Complete walkthrough from spiking to shell access
- **20+ HackTheBox Machines** — Documented walkthroughs including Legacy, Blue, Lame, Devel, Jerry, Nibbles, Optimum, Bashed, Shocker, Valentine, and more
