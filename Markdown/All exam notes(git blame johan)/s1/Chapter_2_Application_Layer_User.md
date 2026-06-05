# Chapter 2: Application Layer — User-Oriented Protocols (Layer 7)

> **Scope note:** This file covers the **user-oriented** application layer protocols — email (X.400, SMTP, POP3, IMAP4), virtual terminals (Telnet, SSH), FTP, HTTP/CGI, and other miscellaneous protocols (NTP, VoIP/SIP, SMB, NFS, RTSP, X11, Wireshark). This is **Semester Test 1** material (Chapter 2). Network-oriented Layer 7 protocols (DNS, SNMP, DHCP, LDAP, routing algorithms) are in Chapter 3 notes.

---

## 1. Network Architectures

The application layer is the *raison d'être* of the network. Services can be arranged in several architectures:

**Client-server architecture** is the dominant model. Servers (known as **dæmons**) listen for and accept requests from clients. A server opens a socket that specifies an address and port number and **waits for connections**.

> **MCQ fact:** The software providing services on the Internet (acting as a server) is often known as a **dæmon**.

**Peer-to-peer (P2P) architecture:** Nodes act as equals; any peer can initiate communication. Classic example: **Napster** (file-sharing). Another example: **MANETs** (Mobile Ad-hoc Networks), used in natural disasters where battery-powered nodes must configure themselves without a central server.

**N-tier (3-tier) architecture:** Data and business logic are moved to a back-end tier (usually a database engine) that is completely separate from the server and client tiers.

> **MCQ fact:** FTP is based on the **client-server** architecture.

---

## 2. Email Protocols

### 2.1 X.400

**X.400** is a series of ITU-T/OSI standards defining a "Message Handling System". It was designed with full awareness of the ISO OSI model and even intended to integrate email with **physical postal delivery (snail mail)**. Still used today in **EDI (Electronic Data Interchange)**.

X.400 uses a complex, hierarchical addressing scheme with components: C (country), ADMD, PRMD, O (organisation), OU (organisational unit), G (given name), S (surname).

### 2.2 SMTP

**SMTP (Simple Mail Transfer Protocol)** is the dominant protocol for *sending* email.

| Detail | Value |
| --- | --- |
| MTA-to-MTA (server-to-server) port | **25** |
| User submission to first MTA | **587** (submit port) |
| After successful `HELO`/`EHLO` | Response code **250** |
| Header/body separator | **Blank line** |
| End-of-message signal | **Full stop on a line of its own** |

> **MCQ fact (2025 ST1 Q17):** The SMTP server returns condition code **250** after successfully handling a `helo` or `ehlo` message.

> **MCQ fact (Addressing):** To send an email to `u@xx.co.za`, the client sends: **`rcpt to: u@xx.co.za`**

> **MCQ fact (Transparency):** The `data` command signals that the payload follows. A full stop on a line of its own ends the body. This creates a transparency problem — a user should avoid typing a full stop on a line of its own, as it will prematurely terminate the message. Modern clients use **dot-stuffing** to work around this.

*Example 1:* Minimal SMTP exchange to send a message:
```
EHLO sender.co.za          → 250 OK
MAIL FROM: <a@sender.co.za> → 250 OK
RCPT TO: <b@xx.co.za>      → 250 OK
DATA                        → 354 Start input
Subject: Test
                            ← blank line separates header from body
Hello there.
.                           ← full stop on a line of its own ends the message
QUIT
```

*Example 2:* If SMTP server X forwards a message to SMTP server Y, server Y will typically use **port 25**.

### 2.3 POP3

**POP3 (Post Office Protocol version 3)** retrieves email. It assumes users manage their mailboxes on their **local computers** (emails are downloaded and usually deleted from the server). Port **110**.

### 2.4 IMAP4

**IMAP4 (Internet Message Access Protocol version 4)** is primarily intended to manipulate a mailbox **on a server**. Allows complex remote folder structures, flags (`\Answered`, `\Seen`), and partial message fetch. Port **143**.

> **MCQ fact (2025 ST1 Q16):** The protocol **primarily intended to manipulate a mailbox on a server** is **IMAP4** (not POP3, which downloads to local).

---

## 3. Virtual Terminal Protocols

Virtual terminal protocols allow a user to use a remote computer as if sitting directly in front of it.

### 3.1 Telnet

**Telnet** provides a virtual terminal service. It transmits all data (including passwords) in **cleartext**. Port **23**.

> **MCQ fact (2023 ST1 Q3a–e):** The specific service offered by Telnet is a **virtual terminal**.

| Test detail | Answer |
| --- | --- |
| Telnet port | **23** |
| Cannot see what you are typing | Adjust **`localecho`** property |
| Manual HTTP via Telnet to `www.example.com` | **`telnet www.example.com 80`** |
| Key combination to open Telnet console/escape | **Escape character** (often `^]`) |

*Example 1:* To manually issue HTTP commands to `www.example.com`:
```
telnet www.example.com 80
GET /index.htm HTTP/1.1
Host: www.example.com
                          ← blank line ends the request
```

*Example 2:* ANSI escape sequences used by dumb terminals:
- `ESC[2J` — clears the screen
- `ESC[y;xH` — moves the cursor to coordinates (y, x)

### 3.2 SSH

**SSH (Secure Shell)** is the encrypted replacement for Telnet. Port **22**. Creator Tatu Ylonen specifically requested port 22 because it sits between FTP (21) and Telnet (23), symbolising a single secure replacement for both.

SSH encrypts all traffic including passwords. Also used as a **tunnelling** protocol (e.g., tunnelling X11 traffic). File transfer via SSH uses the `scp` (secure copy) command.

---

## 4. FTP (File Transfer Protocol)

**FTP (File Transfer Protocol)** transfers files across the network. **Anonymous FTP** allows public access using username `anonymous` or `ftp`.

FTP is unique in using **two separate TCP connections**:

| Connection | Port | Purpose |
| --- | --- | --- |
| Control connection | **21** | Commands and responses |
| Data connection | **20** | Actual file transfer |

**Passive mode (PASV):**

> **MCQ fact (2025 ST1 Q19):** To avoid the need for the **data** channel to connect to the FTP **client**, FTP **passive** mode should be used. In passive mode, the server opens a random port and the client connects to it instead. *(Distractor: "control, passive" — wrong. It is the data channel that is the issue.)*

*Example 1:* Active mode: server's port 20 initiates connection to client → may fail through firewalls/NAT.
*Example 2:* Passive mode: client initiates both connections → works through firewalls.

---

## 5. The Web, HTTP, and CGI

### 5.1 HTTP

**HTTP (Hypertext Transfer Protocol)** is the primary protocol for the Web. Port **80**.

> **MCQ fact:** HTTP fits strictly on the **Application Layer (Layer 7)**.

> **MCQ fact (The Host field):** The primary reason for including the `Host:` header in HTTP is to **enable virtual hosting** — a single server may host many websites on the same IP address, and must know which one to serve. *(Distractor: "there is no Host header" or "it is for security" — wrong.)*

*Example 1:* Valid HTTP request:
```
GET /index.htm HTTP/1.1
Host: www.xx.co.za
                          ← blank line ends the request
```

*Example 2:* HTTP response:
```
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 5667

<!DOCTYPE HTML>
...
```
The `200 OK` status means success. `404 Not Found` means the resource does not exist. A **blank line** separates the response header from the payload.

### 5.2 CGI

**CGI (Common Gateway Interface)** allows web servers to run external programs and return their output to the browser.

> **MCQ fact (2025 ST1 Q18):** A CGI program:
> - **(i) Sends output to a browser by writing to standard output.**
> - **(ii) Receives input from a browser by reading an environment variable set by the server.**
>
> *(Distractors: "reads from standard input" — wrong for input; "writes to socket" — wrong for output.)*

---

## 6. Other Application Layer Protocols

| Protocol | Full Name | Key Fact |
| --- | --- | --- |
| **TFTP** | Trivial File Transfer Protocol | Very simple; used by diskless computers to boot OS images from a server over **UDP**. |
| **NTP** | Network Time Protocol | Obtains current time from a trusted time server. Uses interesting mechanisms to correct for network delay. |
| **SIP** | Session Initiation Protocol | Establishes and terminates **VoIP** (Voice over IP) telephone calls. |
| **SMB / Samba** | Server Message Block | Mounts remote file systems; popular in Microsoft environments. **Samba** is the Unix server implementation. |
| **NFS** | Network File System | Mounts remote file systems; popular in Unix environments. |
| **RTSP** | Real Time Streaming Protocol | Streams multimedia (e.g., Internet radio). |
| **X11 / X Window** | X Window System | Displays graphical output from a remote computer on a local screen. The remote computer is the **client**; the local display is the **server** (counterintuitive). Often tunnelled through SSH. |

> **MCQ fact (2025 ST1 Q20 context):** An SNMP agent is **both a client and a server** — it pushes Traps to the manager (acting as client) and accepts Get/Set requests from the manager (acting as server). The answer is "more than one of the above".

---

## 7. Traffic Sniffing

It is easy to inspect traffic reaching your own computer. **Wireshark** is the popular application used to inspect (sniff) traffic that flows on a network.

> **MCQ fact (2025 ST1 Q15 equivalent):** The popular application used to **inspect traffic that flows on a network** is **Wireshark** (not nslookup, traceroute, ping, or netstat).

> **MCQ fact (Wiretapping law):** The South African Act that specifically regulates "wiretapping" is **RICA** (Regulation of Interception of Communications and Provision of Communication-Related Information Act). *(Distractor: POPIA — that governs personal information, not interception.)*

---

## 8. Well-Known Port Numbers

Memorise these — they appear on every test.

| Port | Protocol | Notes |
| --- | --- | --- |
| 20 | FTP (data) | |
| 21 | FTP (control) | |
| 22 | SSH | |
| 23 | Telnet | |
| 25 | SMTP | MTA-to-MTA |
| 43 | WHOIS | |
| 53 | DNS | |
| 80 | HTTP | |
| 110 | POP3 | |
| 143 | IMAP4 | |
| 587 | SMTP (submit) | User to first MTA |

---

## Examinable Practice Questions

### Multiple Choice

**Q1.** The software providing services on the Internet (acting as a server waiting for client requests) is often known as a:
A. Router   B. Dæmon   C. Daemon Process   D. Agent   E. Proxy

**Q2.** Which of the following protocols is primarily intended to manipulate a mailbox on a server?
A. IMAP4   B. POP3   C. SMTP   D. More than one of the above   E. All of the above

**Q3.** Which condition code will be returned by an SMTP server after successfully handling a `HELO` or `EHLO` message?
A. 0   B. 150   C. 250   D. 350   E. 450

**Q4.** The specific service offered by the Telnet protocol is a:
A. Secure encrypted connection   B. File transfer   C. Virtual terminal   D. Mail relay   E. Domain name resolution

**Q5.** Suppose you want to use a Telnet client to interact with `www.example.com` using HTTP commands. The full command to enter at the CLI is:
A. `telnet www.example.com`   B. `telnet www.example.com 23`   C. `telnet www.example.com 80`   D. `telnet http://www.example.com`   E. `telnet www.example.com 443`

**Q6.** To avoid the need for the ... channel to connect to the FTP client, FTP ... mode should be used.
A. data, passive   B. data, indirect   C. data, reversed   D. control, passive   E. control, indirect

**Q7.** (i) How does a CGI program send output to a browser? (ii) How does a CGI program receive input from a browser?
A. (i) Writes to standard output; (ii) Reads from standard input
B. (i) Writes to the appropriate socket; (ii) Reads from standard input
C. (i) Writes to standard output; (ii) Reads from the appropriate socket
D. (i) Writes to the appropriate socket; (ii) Reads from the appropriate socket
E. (i) Writes to standard output; (ii) Reads an environment variable set by the server

**Q8.** FTP is based on the ... architecture.
A. Client-server   B. Peer-to-peer   C. Client-server-client-server   D. Host-to-host   E. Multitier

**Q9.** The popular application used to inspect traffic that flows on a network is:
A. SniffAndSnort   B. Telnet   C. nslookup   D. tracert / traceroute   E. Wireshark

**Q10.** Which South African Act specifically regulates "wiretapping"?
A. POPIA   B. RICA   C. PAIA   D. The Constitution   E. The Bill of Rights

**Q11.** After an SMTP client has sent a `data` command, it signals that the entire data block has been transmitted by sending the following line:
A. `/data`   B. `quit`   C. `.` (full stop on a line of its own)   D. A blank line   E. `fin`

**Q12.** The `Host:` line in an HTTP GET request is necessary primarily because:
A. Security (access control)   B. Security (integrity)   C. Virtual hosting — the server may host more than one site   D. There is no such `Host:` header   E. There is no GET request in HTTP

### Long-Form & Calculation

**Q13. Telnet session.** [5]
Suppose you open a Telnet connection to a host. Answer the following:
- a) What is the specific service offered by the Telnet protocol?
- b) What port does Telnet use?
- c) You can see the output of your commands, but you cannot see what you are typing. Which property should you adjust to fix this?
- d) Write the full CLI command to open a Telnet connection to `www.example.com` in order to issue HTTP commands manually.
- e) What is the term for the character combination displayed by the Telnet client that you can enter to open the Telnet console?

**Q14. SMTP exchange.** [4]
- a) What command does an SMTP client send to tell the server the recipient's address?
- b) What separates the header from the body of an email transmitted by SMTP?
- c) How does the SMTP client signal the end of the message body?
- d) Explain the transparency problem with SMTP and briefly explain how modern clients work around it.

---

## Memo / Answer Key

### MCQ Answers

**A1.** B (Dæmon).
**A2.** A (IMAP4 — it is specifically designed to manipulate a mailbox on a server).
**A3.** C (250 — standard SMTP success code for HELO/EHLO).
**A4.** C (Virtual terminal).
**A5.** C (`telnet www.example.com 80` — HTTP runs on port 80).
**A6.** A (data, passive — the data channel is the problem; passive mode inverts who connects).
**A7.** E (Writes to standard output; reads an environment variable set by the server).
**A8.** A (Client-server).
**A9.** E (Wireshark).
**A10.** B (RICA).
**A11.** C (Full stop on a line of its own).
**A12.** C (Virtual hosting — the server may host more than one site on the same IP).

### Long-Form Answers

**A13. Telnet session.**
- a) **Virtual terminal**
- b) **23**
- c) **`localecho`**
- d) **`telnet www.example.com 80`**
- e) **Escape character** (often `^]`)

**A14. SMTP exchange.**
- a) **`rcpt to: u@xx.co.za`** (or whatever address)
- b) **A blank line** separates the header from the body.
- c) **A full stop on a line of its own** (`.`)
- d) The problem: if the email body itself contains a line with only a full stop, SMTP treats it as end-of-message, truncating the body prematurely. Modern clients use **dot-stuffing** — inserting an extra dot before any line that starts with a dot — so a body line of `.` becomes `..` on the wire, and the extra dot is stripped at the destination.
