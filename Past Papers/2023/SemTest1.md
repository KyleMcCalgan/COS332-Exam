# University of Pretoria
## COS 332 — Computer Science
### Semester Test: 13 March 2023

**Time:** 1 hour  
**Marks:** 40  
**Examiner:** Prof MS Olivier  
**This paper consists of 8 pages.**

---

**Instructions:**
- Answer all questions.
- No calculators permitted.
- You are allowed to write on this test paper.

---

## Question 1

*In each case select the alternative that fits the question best and write only the corresponding letter on your answer sheet.*

**a)** A proprietary network protocol is a protocol that

- A: Has been standardised by some national standards body.
- B: Is owned by a specific vendor.
- C: Is developed as an open source protocol.
- D: Is now so old that using it has been deprecated.
- E: Describes the properties of other network protocols.

---

**b)** Which of the following characters is not present in standard ASCII?

- A: A
- B: &
- C: #
- D: £
- E: ~

---

**c)** Suppose node X communicates with node Z. A header is added at layer n at X. This header may be removed by

- A: Layer n at Z.
- B: Layer n − 1 at X.
- C: Layer n + 1 at X.
- D: Layer n − 1 at Z.
- E: More than one of the above

---

**d)** Which ISO layer enables process-to-process communication via the network?

- A: 6
- B: 5
- C: 4
- D: 3
- E: 2

---

**e)** A layer on a protocol stack communicates with its peer layer. Suppose node X sends a message to node Y. Which node's (or nodes') layer 3 is/are deemed to be the peer(s) of layer 3 of X?

- A: Only Y.
- B: All the nodes on the path after X, up to and including Y.
- C: All the nodes on the path from X (including X), up to and including Y.
- D: Only the router nodes on the path after X, up to and including Y, which excludes most nodes on this path.
- E: Only the router nodes on the path from X (including X), up to and including Y, which excludes most nodes on this path.

---

**f)** On which OSI layer(s) is error checking primarily performed?

- A: 7
- B: 2
- C: Application-oriented layers
- D: Network-oriented layers
- E: All seven layers

---

**g)** The OSI layer that, amongst others, attempts to emulate database transactions where messages can be 'rolled back' if the final message in a sequence is not sent, is layer

- A: 2
- B: 3
- C: 4
- D: 5
- E: 6

---

**h)** Which protocol is primarily intended to manipulate a mailbox on a server?

- A: IMAP4
- B: POP3
- C: SMTP
- D: More than one of the above
- E: All of the above

---

**i)** The `capetown.` sTLD has to adhere to policies prescribed by

- A: ICANN
- B: ZADNA
- C: ISO
- D: More than one of the above
- E: All of the above

---

**j)** The SMTP submit port is

- A: 25
- B: 100
- C: 443
- D: 587
- E: None of the above

---

**k)** With which architecture was the *Napster* service associated?

- A: Client-server
- B: Peer-to-peer
- C: 3-tier
- D: 4-tier
- E: 5-tier

---

**l)** The popular network software known as `bind`

- A: Acts as a name server.
- B: Connects two processes to facilitate communication.
- C: Associates a process with a port.
- D: Is used to authenticate a user.
- E: More than one of the above

---

**m)** When a server opens a socket for communication with a remote host, it needs to supply

- A: The port number on the remote host.
- B: The address of the remote host.
- C: The port number on the local host.
- D: More than one of the above
- E: All of the above

---

**n)** If the FQDNs of DNS root name servers are ordered lexicographically, the last entry in the list is

- A: l.dns.net
- B: m.dns.net
- C: n.dns.net
- D: l.root-servers.net
- E: m.root-servers.net

---

**o)** An agent that monitors and controls network activity in an SNMP-managed network node, is a(n)

- A: Client
- B: Server
- C: P2P-node
- D: More than one of the above
- E: All of the above

---

**p)** Which condition code will be returned by an SMTP server after successfully handling a `helo` or `ehlo` message?

- A: 0
- B: 150
- C: 250
- D: 350
- E: 450

---

**q)** The bulk, if not all, of the resource records in the DNS root name servers are of the following type(s):

- A: A
- B: MX
- C: NS
- D: More than one of the above
- E: All of the above

---

**r)** Which of the following is a popular application used to inspect traffic that flows on a network?

- A: SniffAndSnort
- B: telnet
- C: nslookup
- D: tracert / traceroute
- E: Wireshark

---

**s)** Which South African Act specifically regulates 'wiretapping'?

- A: POPIA
- B: RICA
- C: PAIA
- D: The Constitution
- E: The Bill of Rights

---

**t)** To avoid the need for the … channel to connect to the FTP client, FTP … mode should be used.

- A: data, passive
- B: data, indirect
- C: data, reversed
- D: control, passive
- E: control, indirect
- F: control, reversed

**[20]**

---

## Question 2

*Consider the SMTP protocol.*

**a)** If SMTP server X forwards a message to SMTP server Y, which well-known port will Y typically use? **(1)**

**b)** Suppose a client wants to send an email to `u@xx.co.za`. What message will be sent to the SMTP server to instruct the server to do so? **(1)**

**c)** An email to be transferred via SMTP will usually consist of a header and a body, as specified in RFC822. What separates the header from the body? **(1)**

**d)** The `data` message is used to indicate that the email itself would be sent next. What does the client send to the server to indicate that it has transmitted the entire message? Use words to describe this 'token' that signifies the end of the message. **(1)**

**e)** Is it possible to send an email to someone where the email includes a full stop on a line of its own? (Yes/No). **(1)**

**[5]**

---

## Question 3

*Consider the Telnet protocol.*

**a)** What is the intended purpose of Telnet? Provide your answer as a descriptive phrase, rather than stating that it enables one to execute commands on remote computers. **(1)**

**b)** Which well-known port is typically used by a Telnet server? **(1)**

**c)** Suppose you are using a Telnet server. The outputs of your commands are displayed correctly. However, whenever you type something at the client, you cannot see what you are typing. Which property should you adjust at the client to rectify the problem? **(1)**

**d)** Suppose you want to use the Telnet client to interact with `www.example.com` using manually entered HTTP commands. Provide the full command you will enter on the command-line interface to open the connection. **(1)**

**e)** When opening a Telnet connection, the Telnet client displays a character combination that one may enter to open the Telnet console. (This is often `^]`.) What is this sequence called by the client? **(1)**

**[5]**

---

## Question 4

*The data link layer is used to logically connect two neighbouring nodes in a network to one another.*

**a)** Name the three primary functions of the data link layer. **(3)**

**b)** Name one example of a data link layer protocol. **(1)**

**c)** Network layers are supposed to be independent, but this is often not possible. Provide an example of how layer 1 may impact on one of the three functions you named at question (a). **(1)**

**[5]**

---

## Question 5

*On the answer sheet you will find a partial zone file for `xx.co.za`. You are expected to add resource records to it to enable the server to provide the answers described below. (Note that you will not repeat `xx.co.za` in any of your answers, because it is known that this zone file deals with `xx.co.za`.)*

**a)** The IP address of `www.xx.co.za` is 10.9.8.7. **(1)**

**b)** Any traffic addressed to `yy.xx.co.za` should be sent to `xx.org.za`. **(1)**

**c)** Mail to any mailbox in `xx.co.za` should preferably be sent to 192.168.1.1. **(1)**

**d)** If 192.168.1.1 is down, mail to any mailbox in `xx.co.za` should be sent to 192.168.99.99. **(1)**

**e)** 172.16.16.16 is a name server for `xx.co.za`. **(1)**

**[5]**

---

**TOTAL: [40]**

---

---

# MEMO — Paper 1 (13 March 2023)

## Question 1 — Answers

| # | Answer |
|---|--------|
| a | B — Is owned by a specific vendor |
| b | D — £ |
| c | A — Layer n at Z |
| d | C — 4 (Transport) |
| e | B — All the nodes on the path after X, up to and including Y |
| f | E — All seven layers |
| g | C — 4 (Transport) |
| h | A — IMAP4 |
| i | D — More than one of the above (ICANN and ZADNA) |
| j | D — 587 |
| k | B — Peer-to-peer |
| l | A — Acts as a name server |
| m | C — The port number on the local host |
| n | E — m.root-servers.net |
| o | D — More than one of the above |
| p | C — 250 |
| q | C — NS |
| r | E — Wireshark |
| s | B — RICA |
| t | D — control, passive |

---

## Question 2 — Memo

**a)** Port **25** (nothing is being submitted; server-to-server SMTP uses port 25).

**b)** `MAIL TO: u@xx.co.za`

**c)** A **blank line** (empty line) separates the header from the body.

**d)** A line consisting of a **full stop on a line of its own** (i.e., `CRLF.CRLF`).

**e)** **Yes** — the full stop must be *doubled* (escaped) so that a lone full stop is not treated as the end-of-message signal; the recipient's server will remove the extra dot.

---

## Question 3 — Memo

**a)** Telnet provides a **virtual terminal** (remote login) facility, allowing a user to interact with a remote computer as though they were at a local terminal.

**b)** Port **23**.

**c)** The **local echo** property should be enabled at the client.

**d)** `telnet www.example.com 80`

**e)** The **escape character** (typically `^]`).

---

## Question 4 — Memo

**a)** Three primary functions of the data link layer:
1. **Framing** (delineation of frames / error delimitation)
2. **Error control** (detection and/or correction of bit errors)
3. **Flow control** (preventing a fast sender from overwhelming a slow receiver)

**b)** Example: **Ethernet** (also acceptable: PPP, HDLC, Wi-Fi/802.11, etc.)

**c)** Example: A noisy medium (layer 1) may introduce bit errors, which means error correction (a layer 2 function) becomes necessary. A good medium that only needs error *detection* on layer 2 may not require error *correction* on layer 2.

---

## Question 5 — Memo

```
www   IN  A      10.9.8.7                        ; (a)
yy    IN  CNAME  xx.org.za.                      ; (b)
@     IN  MX  5  192.168.1.1                     ; (c)  (lower number = higher preference)
@     IN  MX  10 192.168.99.99                   ; (d)
@     IN  NS     172.16.16.16                    ; (e)
```

*(MX priority numbers may vary as long as 192.168.1.1 has the lower/preferred value.)*
